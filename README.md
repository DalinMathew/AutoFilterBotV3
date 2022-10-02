

![GitHub Repo stars](https://img.shields.io/github/stars/DalinMathew/AutoFilterBotV3?style=social)
<img src="https://img.shields.io/github/forks/DalinMathew/AutoFilterBotV3?style=social"></img>
## How To Deploy Video
<a href="https://youtu.be/5hnYOKBzyi8"><img src="https://img.shields.io/badge/How%20To%20Deploy-blue.svg?logo=Youtube"></a> <img src="https://img.shields.io/youtube/views/5hnYOKBzyi8?style=social">
## Subscribe YouTube Channel
<a href="https://youtube.com/NaughtyPROFESSOR"> <img src="https://img.shields.io/youtube/channel/subscribers/UCU3Hg3qJJrIaC_0Gw7MLT1A?V?label=Subscribers&style=for-the-badge&color=red&labelColor=ce463"/> </a>

#### Added Features
* Imdb posters for autofilter.
* Imdb rating for autofilter.
* Custom captions for your files.
* Index command to index all the files in a given channel (No USER_SESSION Required).
* Ability to Index Public Channels without being admin.
* Support Auto-Filter (Both in PM and in Groups)
* Once files saved in Database , exists until you manually deletes. (No Worry if post gets deleted from source channel.)
* Added Force subscribe (Only channel subscribes can use the bot)
* Ability to restrict groups(AUTH_GROUPS)

#### Deploy To Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Pooja0033/AutoFilterBotV3)

#### Hard Way
```bash
# Create virtual environment
python3 -m venv env

# Activate virtual environment
env\Scripts\activate.bat # For Windows
source env/bin/activate # For Linux or MacOS

# Install Packages
pip3 install -r requirements.txt

# Edit info.py with variables as given below then run bot
python3 bot.py
```
Check [`sample_info.py`](sample_info.py) before editing [`Config.py`](Config.py) file

### Variables

#### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com)

#### Optional Variables
* `OMDB_API_KEY`: OMBD_API_KEY to generate imdb poster for filter results.Get it from [omdbapi.com](http://www.omdbapi.com/apikey.aspx)
* `CUSTOM_FILE_CAPTION` : A custom caption for your files. You can format it with file_name, file_size, file_caption.(supports html formating)
Example: `<b>Join [MT Bots](https://t.me/MalRok) for Best Channels</b>\n\n<code>{file_name}</code>\nSize{file_size}\n{file_caption}.`
* `AUTH_GROUPS` : ID of groups which bot should work as autofilter, bot can only work in thease groups. If not given , bot can be used in any group.
* `COLLECTION_NAME`: Name of the collections. Defaults to Telegram_files. If you going to use same database, then use different collection name for each bot
* `CACHE_TIME`: The maximum amount of time in seconds that the result of the inline query may be cached on the server
* `USE_CAPTION_FILTER`: Whether bot should use captions to improve search results. (True/False)
* `AUTH_USERS`: Username or ID of users to give access of inline search. Separate multiple users by space. Leave it empty if you don't want to restrict bot usage.
* `AUTH_CHANNEL`: ID of channel. Without subscribing this channel users cannot use bot.
* `START_MSG`: Welcome message for start command.

##### Note
* Currently [API used](http://www.omdbapi.com) here is allowing 1000 requests per day. [You may not get posters if its crossed]. 
Once a poster is fetched from OMDB , poster is saved to DB to reduce duplicate requests.

## Tips
* You can use `|` to separate query and file type while searching for specific type of file. For example: `Avengers | video`
* If you don't want to create a channel or group, use your chat ID / username as the channel ID. When you send a file to a bot, it will be saved in the database.

## Thanks to 
* [Pyrogram](https://github.com/pyrogram/pyrogram)
* [Original Repo](https://github.com/Mahesh0253/Media-Search-bot)
* [subinps](https://github.com/subinps/Media-Search-bot)
* [Editing Muhammed Rk](https://github.com/PR0FESS0R-99/LuciferMoringstar_Robot)
* [Mo Tech YT](https://t.me/Mo_Tech_Group)
* [Lucifer Morningstar](@Lucifer_Devil_AD)

## License
Code released under [The GNU General Public License](LICENSE).
