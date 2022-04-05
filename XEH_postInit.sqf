#include "script_component.hpp"
if !(GVAR(enable)) exitWith { INFO("COALITION Twitch Bot disabled"); };

diag_log format ["[COALITION TWITCH BOT]: Starting client post init [%1]",diag_tickTime];

// Get chat connection settings from CBA
_channelName = QGVAR(channelName);
_oAuthKey = QGVAR(oAuth);
_nickName = QGVAR(nickName);

// Call python function here - return true if connected
/* _enableChat = ["CoalitionChatBot.connectToTwitch", [_channelName, _oAuthKey, _nickName]] call py3_fnc_callExtension;

if (_enableChat) then {
	systemChat format ["[CTB ACTIVE] Showing chat from: %1",GVAR(channelName)];
} else {
	systemChat "[CTB ERROR] Failed to connect to chat. Check settings!";
}; */

diag_log format ["[COALITION TWITCH BOT]: Client post init complete [%1]",diag_tickTime];