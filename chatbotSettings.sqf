[
	QGVAR(enable),
    "CHECKBOX",
    ["Enable Twitch Chat", "Enables reading of twitch chat messages from your chat"],
    "COALITION Twitch Bot - General",
    true,
    true, 
	{
        [QGVAR(enable), _this] call EFUNC(common,cbaSettings_settingChanged)
    },
    true
] call CBA_Settings_fnc_init;

[
	QGVAR(channelName),
    "EDITBOX",
    ["Channel to Monitor", "Enter a channel name exactly how it is on twitch with a hashtag. IE: #tanakaTV"],
    "COALITION Twitch Bot - General",
    "",
    true, 
	{
        [QGVAR(channelName), _this] call EFUNC(common,cbaSettings_settingChanged)
    },
    true
] call CBA_Settings_fnc_init;

[
	QGVAR(nickName),
    "EDITBOX",
    ["Twitch Account Name", "Enter in your twitch account name"],
    "COALITION Twitch Bot - Private",
    "",
    true, 
	{
        [QGVAR(nickName), _this] call EFUNC(common,cbaSettings_settingChanged)
    },
    true
] call CBA_Settings_fnc_init;

[
	QGVAR(oAuth),
    "EDITBOX",
    ["OAuth Key", "Enter in your oauth key generated from twitchapps.com/tmi/"],
    "COALITION Twitch Bot - Private",
    "",
    true, 
	{
        [QGVAR(oAuth), _this] call EFUNC(common,cbaSettings_settingChanged)
    },
    true
] call CBA_Settings_fnc_init;