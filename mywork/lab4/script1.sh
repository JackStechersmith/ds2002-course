#!/bin/bash

clear


curl https://9b16f79ca967fd0708d1-2713572fef44aa49ec323e813b06d2d9.ssl.cf2.rackcdn.com/1140x_a10-7_cTC/Pirates-Red-Sox-Baseball-20-1692921973.jpg > oneil.png
aws s3 cp oneil.png s3://ds2002-svc8ft/

aws s3 presign --expires-in 604800 s3://ds2002-svc8ft/oneil.png

https://ds2002-svc8ft.s3.us-east-1.amazonaws.com/oneil.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA3FLD3OOGP227HYEZ%2F20240315%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240315T190931Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDA7Kg7KcVFtAmNa4QCLEAdZzr7vay%2FrBVMIowpSPNRMx5UW9WU%2FRs5P5cXYKdrN6vj6RRpLSVUxrjq4Eo0jjXcg2ADFHk4MxFks4IDZuV5SouwKudJNvzOM4lqUc1qHcxIV%2FfIoYPMwojyqhvIGTjj%2FhNALjOomXRPE23qtWRnQmnTJHLgMypfTUdJFGUJy7AnD6WlWDj6zlrOSKhY7IAHFHfytjFzosq8AX%2FVm6Xvr9gLIh7XXRJUfO4y5U2rzP1RNKOEhYykdIQxJdHzu%2FvfZPxhAo%2BrLSrwYyLZy%2FXEntGn3bPKR%2B1MQJyhF6PdrTbCjjVK631dHHv5L4RgpGRMwr9nLe%2FvrANw%3D%3D&X-Amz-Signature=9d4dd5effee53bb27a880082e1192438ab1d50ac57d3bbd9faa3f85505880ea6