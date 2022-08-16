#!/usr/bin/python

import httplib2
import sys
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
import google_auth_oauthlib.flow

FILE_PATH = os.path.abspath(__file__)
VIDEO_DIR = os.path.dirname(FILE_PATH)
INFRA_DIR = os.path.dirname(VIDEO_DIR)
SRC_DIR = os.path.dirname(INFRA_DIR)
ROOT_DIR = os.path.dirname(SRC_DIR)
CLIENT_SECRETS_FILE = os.path.join(ROOT_DIR, ("client_secrets.json"))
OAUTH_DIR = os.path.join(VIDEO_DIR, ("oauth2.json"))
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

%s

with information from the API Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % CLIENT_SECRETS_FILE

YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


class YoutubeApi(object):
    def __init__(self):
        pass

    def initialize_api(self):
        try:
            flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                           scope=YOUTUBE_READ_WRITE_SCOPE,
                                           message=MISSING_CLIENT_SECRETS_MESSAGE)
            storage = Storage(OAUTH_DIR)
            credentials = storage.get()
            if credentials is None or credentials.invalid:
                credentials = run_flow(flow, storage, argparser.parse_args())
            return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                         http=credentials.authorize(httplib2.Http()))
        except Exception as e:
            raise e

    # ////////////////////////////////////////////////////////////////////////////// PLAYLIST //////////////////////////////////////////////////////////////////////////////

    def list_playlist(self):
        youtube = self.initialize_api()
        request = youtube.playlists().list(part="id, snippet, status",
                                           channelId="UCmePd2U1QGDYQysI8xqe1XA", maxResults=50)
        response = request.execute()
        print(response)
        return response

    def delete_playlist(self, id):
        youtube = self.initialize_api()
        request = youtube.playlists().delete(id=id)
        response = request.execute()
        print(response)
        return response

    def create_playlist(self, title, description):
        try:
            youtube = self.initialize_api()
            request = youtube.playlists().insert(
                part="snippet, status",
                body={
                    "snippet": {
                        "title": f"{title}",
                        "description": f"{description}"
                    },
                    "status": {
                        "privacyStatus": "public"
                    }
                }
            )
            response = request.execute()
            print(response)
            return response
        except Exception as e:
            raise Exception("An HTTP error %d occurred:\n%s" %
                            (e.resp.status, e.content))

    # ////////////////////////////////////////////////////////////////////////////// PLAYLIST ITEMS //////////////////////////////////////////////////////////////////////////////

    def list_playlist_items(self, playlistId):
        youtube = self.initialize_api()
        request = youtube.playlistItems().list(part="id, snippet, contentDetails, status",
                                               playlistId=f"{playlistId}", maxResults=50)
        response = request.execute()
        print(response)
        return response

    def insert_playlist_items(self, videoId, playlistId):
        youtube = self.initialize_api()
        request = youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": f"{playlistId}",
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": f"{videoId}"
                    }}}
        )

        response = request.execute()
        print(response)
        return response

    def update_playlist_items(self, videoId, playlistId):
        youtube = self.initialize_api()
        request = youtube.playlistItems().update(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": f"{playlistId}",
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": f"{videoId}"
                    }}}
        )

        response = request.execute()
        print(response)
        return response

    def delete_playlist_items(self, id):
        youtube = self.initialize_api()
        request = youtube.playlistItems().delete(id=id)
        response = request.execute()
        print(response)
        return response


if __name__ == '__main__':
    yt = YoutubeApi()
    yt.create_playlist("test", "01")
