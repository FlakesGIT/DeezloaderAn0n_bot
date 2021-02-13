#!/usr/bin/python3

from telegram import InlineKeyboardButton

not_interface = False
default_time = 0.0
channel = -1001215335384
roots = [1314948019]
limit = 2000000000
seconds_limits_album = 40000
max_songs = 400
telegram_file_api_limit = 1500000000
telegram_audio_api_limit = 50000000
db_file = "dwsongs.db"
loc_dir = "Songs/"
ini_file = "settings.ini"
photo = "https://i.pinimg.com/originals/e3/39/35/e339352ea8faf949945369a35493a413.png"
bot_name = "DeezerFlixBot"
api_chart = "https://api.deezer.com/chart"
api_artist = "https://api.deezer.com/artist/%s"
api_type1 = "https://api.deezer.com/search/{}/?q={}"
api_type2 = "https://api.deezer.com/search/?q={}:\"{}\""
song_default_image = "https://e-cdns-images.dzcdn.net/images/cover/1800x1800-000000-80-0-0.jpg"
services_supported = ["spotify", "deezer"]
comandss = ["start", "settings", "info", "shazam", "help"]
settingss = ["quality", "tongue"]
qualities = ["FLAC", "MP3_320", "MP3_256", "MP3_128"]
send_image_track_query = "🎧 Track: %s \n👤 Artist: %s \n💽 Album: %s \n📅 Date: %s"
send_image_album_query = "💽 Album: %s \n👤 Artist: %s \n📅 Date: %s \n🎧 Total Tracks: %d"
send_image_artist_query = "👤 Artist: %s \n💽 Album Numbers: %d \n👥 Fans On Deezer: %d"
tags_query = "💽 Album: %s\n📅 Date: %s\n📀 Label: %s\n🎵 Genre: %s"
info_msg = "🔺 Version: %s\n🔻 Bot Name: @%s\n🤖 Support Bot: @%s\n📢 Support Channel: %s\n🧕 Created By: %s\n👥 Total Users: %d\n⬇️ Total Downloads: %d"
send_image_playlist_query = "📅 Creation: %s \n👤 User: %s \n🎧 Tracks Amount: %d"
insert_query = "INSERT INTO DWSONGS (id, query, quality) values ('%s', '%s', '%s')"
where_query = "SELECT query FROM DWSONGS WHERE id = '{}' and quality = '{}'"
user_exist = "SELECT chat_id FROM CHAT_ID where chat_id = '%d'"
share_message = "tg://msg?text=Start @%s for download all the songs which you want ;)" % bot_name
start_message = "Welcome to @%s \nPress '/' to get commands list" % bot_name
not_supported_links = "Sorry :( The bot doesn't support this link %s :("
rate_link = "https://t.me/FlixBots"
end_message = "ALL FILES UPLOADED SUCCESSFULLY 🥳\n\nJoin Our Updates Channel ☛︎ @FLIXBOTS"

help_message = (
	 "WELCOME TO DEEZER FLIX BOT 🥳\n\nHere's a list of commands I can use -\n/start - Start the bot\n/settings - Manage settings\n/shazam - Identify from Audio\n/help - Show this message\n/info - Show Info\n\nYou may do any of the following while talking to me -\n• Send a Spotify or Deezer Link\n• Type the name of the song directly\n• Use an inline command to search\n• Send an Audio file\n\nSubscribe To @FlixBots If You ❤️ This Bot"
)

end_keyboard = [
	[
		InlineKeyboardButton(
			"🍀 SHARE THIS BOT 🍀",
			url = share_message
		)
	]
]

qualities_keyboard = [
	[
		InlineKeyboardButton(
			qualities[a],
			callback_data = qualities[a]
		),
		InlineKeyboardButton(
			qualities[a + 1],
			callback_data = qualities[a + 1]
		)
	] for a in range(
		0, len(qualities), 2
	)
]

first_time_keyboard = [
	[
		InlineKeyboardButton(
			"🎶 𝗝𝗢𝗜𝗡 𝗙𝗟𝗜𝗫 𝗕𝗢𝗧𝗦 🎶",
			url = "t.me/flixbots"
		)
	]
]

queries = {
	"top": {
		"query": "%s/top?limit=30",
		"text": "TOP 30 🔝"
	},

	"albums": {
		"query": "%s/albums",
		"text": "ALBUMS 💽"
	},

	"radio": {
		"query": "%s/radio",
		"text": "RADIO 📻"
	},

	"related": {
		"query": "%s/related",
		"text": "RELATED 🗣"
	},

	"download": {
		"text": "Download ⬇️"
	},

	"info": {
		"text": "Info ❕"
	},

	"back": {
		"text": "BACK 🔙"
	},

	"s_art": {
		"query": "art: %s",
		"text": "Search By Artist 👤"
	},

	"s_alb": {
		"query": "alb: %s",
		"text": "Search By Album 💽"
	},

	"s_pla": {
		"query": "pla: %s",
		"text": "Search Playlist 📂"
	},

	"s_lbl": {
		"query": "lbl: %s",
		"text": "Search Label 📀"
	},

	"s_trk": {
		"query": "trk: %s",
		"text": "Search Track 🎧"
	},

	"s_": {
		"query": "%s",
		"text": "Global Search 📊"
	}
}
