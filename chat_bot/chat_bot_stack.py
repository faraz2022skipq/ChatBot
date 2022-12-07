from aws_cdk import (
    Stack,
    Duration,
    aws_lex as lex_,
    aws_lambda as lambda_
)
from constructs import Construct

class ChatBotStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        chatbot = lex_.CfnBot(self, "WeatherAPI",
            data_privacy = {"ChildDirected": False},
            idle_session_ttl_in_seconds = 300,
            name = "WeatherAPI",
            role_arn = "arn:aws:iam::136037166860:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots")
        
    # Defining my create_lembda function
    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_lambda/README.html
    def create_lambda(self, id_, path, handler, role):
        '''
            This will take my desired action of Lambda function performing code 
            and will deploy it on cloud
        '''
        return lambda_.Function(self,
            id = id_,
            code = lambda_.Code.from_asset(path),
            handler = handler,
            runtime = lambda_.Runtime.PYTHON_3_8,
            role = role,
            timeout = Duration.seconds(30)
        )