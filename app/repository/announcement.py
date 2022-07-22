from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource


class AnnouncementRepository:
    
    def __init__(self, db: ServiceResource) -> None:
        self.__db = db 

    def get_all(self):
        table = self.__db.Table('Announcement')
        response = table.scan()
        return response.get('Items', [])

    def get_announcement(self, uid: str):
        try:
            table = self.__db.Table('Announcement')
            response = table.get_item(Key={'uid': uid})
            return response['Item']
        except ClientError as e:
            raise ValueError(e.response['Error']['Message'])

    def create_announcement(self, announcement: dict):
        table = self.__db.Table('Announcement')
        response = table.put_item(Item=announcement)
        return response

    def update_announcement(self, announcement: dict):
        table = self.__db.Table('Announcement')  
        response = table.update_item(
            Key={'uid': announcement.get('uid')},
            UpdateExpression="""                
                set
                    title=:title,
                    description=:description,
                    date=:date
            """,
            ExpressionAttributeValues={
                ':title': announcement.get('title'),
                ':description': announcement.get('description'),
                ':date': announcement.get('date')
            },
            ReturnValues="UPDATED_NEW"
        )
        return response

    def delete_announcement(self, uid: str):
        table = self.__db.Table('Announcement')
        response = table.delete_item(
            Key={'uid': uid}
        )
        return response
