from pubnub import Pubnub

__author__ = 'venkat'


pubnub =Pubnub(publish_key='pub-c-ea0f3abe-5fb4-4271-93e5-82e99f464336',
                subscribe_key='sub-c-c73945b8-1716-11e6-b700-0619f8945a4f')

channel="my_channel"

item_code = "M1"
moq = 200
item_wt = 0

pubnub.publish(channel=channel, message=str(item_wt)+ " " + item_code + " " + str(moq))