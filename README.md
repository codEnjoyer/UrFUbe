# UrFU(be) like:
* Cloude storage - yandex cloud

## API Project
### Models
#### User

- name
- user-id
- videos
- role: customer / admin

#### Video

- title
- status: for-authorized / for-all / for-myself
- video-id
- likes and dislikes
- comments

### Endpoints

#### Authorization
**POST _/login <login, password, more params>_** - create an account

**GET _/login <login, password>_** - login, create session

**DELETE _/login_** - logout, delete session

#### Watch video
**GET _/video/<video_id>_** - request to issue video for this request

**GET _/search <text of request>_** - query to search for a video (gives a list of Video)

#### Upload video
**POST _/user/add_video_** - video upload (creates a unique video_id on the server)

**DELETE _/user/delete_video/<video_id>_** - delete video 

#### Comments
**GET _/user/<user_id>/comments_** - get user's comments 

**POST _/video/<video_id>/comments/add <comment text>_** - add comment

**DELETE _/video/<video_id>/comments/<comment_id>_** - delete comment

#### Likes
**POST _/video/<video_id>/<like/dislike>_** - add like/dislike
