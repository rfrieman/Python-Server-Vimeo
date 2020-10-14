# Python-Server-Vimeo
There's an embedded Vimeo video on a website that shows the previous day's weather timelapse. Instead of changing the embedded file source daily, we decided to write a Python script that uses Vimeo's "replace video source file" option. The documentation here describes the process of becoming an "app developer" and using that freedom to automate a daily video source replacement.

As of October 14, 2020, this script is as barebones as it gets, while still achieving the desired effect. There is no error reporting, there is no metadata editing. The thumbnail for the video remains constant and was uploaded via Vimeo's GUI.

In order to even consider implementing a solution like this, you must become an "Adpplication Developer" for VImeo. Instructions for doing getting set up are present on Vimeo's API quick start guide: https://developer.vimeo.com/api/guides/start

https://developer.vimeo.com/apps

As stated in the guide, you'll also need to apply for an Authorized Token. Be sure to specify the following "scopes": private edit delete upload public. This will allow your "app" to re-upload/replace the video source. Once granted, copy and save the Token, because it becomes hashed out and you can't see it again.

Under the section "making your first Vimeo API Call" I found the code to be lacking for Python. The HTTP code specifies a website to navigate to for a response, which is unauthorized unless your Token, Key and Secret are legitimate. Specify https://api.vimeo.com/tutorial for a destination to get a response.

