from aws_cdk import (
    Stack,
    Duration,
    aws_iam as iam_,
    aws_lex as lex_,
    aws_lambda as lambda_
)
from constructs import Construct

class ChatBotStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        chatbot = lex_.CfnBot(self, "WeatherBot",
            data_privacy = {"ChildDirected": False},
            idle_session_ttl_in_seconds = 300,
            name = "WeatherBot",
            role_arn = "arn:aws:iam::136037166860:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots")
        
        # Calling role funtion that will give Lambda "full Lex access"
        lambda_role = self.lambda_role()
        weatherlambda = self.create_lambda("weatherlambda", "./resources", "weatherlambda.lambda_handler", lambda_role)

        
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

    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_iam/Role.html
    def lambda_role(self):
        lambda_role = iam_.Role(self, "Role",
            assumed_by = iam_.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies = [
                    iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonLexFullAccess")
            ]
)