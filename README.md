# SNS Pipe

Publishes standard input to an [Amazon SNS](http://aws.amazon.com/sns/) topic.


# Installation

    pip install sns-pipe


# Configuration

SNS Pipe uses Boto 3, which requires configuration.

See https://boto3.readthedocs.org/


# Usage

    echo hello | sns-pipe $SNS_TOPIC_ARN
