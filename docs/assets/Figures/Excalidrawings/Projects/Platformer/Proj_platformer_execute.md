---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data
## Text Elements
execute() ^jDsLhi3d

updateLogic() ^6TcqV1lj

updateAnimations() ^imKoOw7t

render() ^UV0Vp3Qp

handleEvents() ^lHdvXDEE

render() ^o3vITPzs

switch(gameState) ^abwRj9k3

currentMenu
->
render(window) ^J2CELgZF

currentLevel
->
render(window) ^P8vvrjyh

player
->
render(window) ^nc0KhXCW

default ^FXUbHnxh

playing ^fF2Q0HTq

pause / game over ^RdCG5fF5

render
this
first ^3oUFhdGC

then
render
this ^jiyW48Gz

GUI
->
render(window) ^mD8LPOfn

handleEvents() ^NZIJlYUv

switch(gameState) ^j6FWgYyx

playing ^f4jdWPse

default ^jnfiiMnx

currentMenu -> handleHover() ^ZlIFeIn9

player
->
handleMovements() ^HttWSyZF

esc ^Nv7YLVQE

no ^x4uxmiig

updateGameState(pause) ^fu7seEmn

yes ^VXmbNf5Z

updateLogic() ^XwTKZB1k

TODO: Physics ^YcZVNcYC

quit ^jzhFQZ9R

trigger_data
= currentMenu ->
handleTrigger() ^uRSQttry

if (trigger_data.new_json) ^xEQofzOQ

save() ^WfFwsMHm

if (trigger_data.new_state
        != currentState) ^qLQAvmAk

updateGameState
(trigger_data.new_state) ^B5u6EgYU

settings = difference_btwn(settings, trigger_data.new_json) ^GbFeVUBV

died ^BnOVqwSl

no ^UdVm3dTi

updateGameState(GameOver) ^LibpxGbs

yes ^Cw5A4CgU

cleanup() ^cKvrVDrv

updateSettings() ^oIuT29Fy

%%
## Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.5.2",
	"elements": [
		{
			"type": "rectangle",
			"version": 74,
			"versionNonce": 932721897,
			"index": "a0",
			"isDeleted": false,
			"id": "jq-2Wv5Fw4EYYe8GJ5ta5",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -162.75,
			"y": -170.9140625,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 345,
			"height": 360.91656775434114,
			"seed": 2008109865,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1736688380763,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 78,
			"versionNonce": 1715747817,
			"index": "a1",
			"isDeleted": false,
			"id": "jDsLhi3d",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -149.75,
			"y": -151.9140625,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 178.19989013671875,
			"height": 45,
			"seed": 2051999241,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1736688310038,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 8,
			"text": "execute()",
			"rawText": "execute()",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "execute()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 262,
			"versionNonce": 276999178,
			"index": "a8",
			"isDeleted": false,
			"id": "eibHsRJwwlAk6nfZVuTs7",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -147.53129129167996,
			"y": -18.39147554089402,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 176.68025774799938,
			"height": 58.133504162244215,
			"seed": 1301931337,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "6TcqV1lj"
				},
				{
					"id": "kGTcvFTRtFb5w_mj4EaEY",
					"type": "arrow"
				}
			],
			"updated": 1740463767663,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 272,
			"versionNonce": 1714054311,
			"index": "a9",
			"isDeleted": false,
			"id": "6TcqV1lj",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -130.6911624176803,
			"y": -1.8247234597719135,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 143,
			"height": 25,
			"seed": 1168135209,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1736689289568,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "updateLogic()",
			"rawText": "updateLogic()",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "eibHsRJwwlAk6nfZVuTs7",
			"originalText": "updateLogic()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 337,
			"versionNonce": 1279325767,
			"index": "aA",
			"isDeleted": false,
			"id": "fzM2fBwrRhRaWiVdc6Uni",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -148.10122760699528,
			"y": 49.43094598172422,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 229.1143987570831,
			"height": 52.020891585574645,
			"seed": 347465481,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "imKoOw7t"
				}
			],
			"updated": 1736688394168,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 370,
			"versionNonce": 1232639335,
			"index": "aB",
			"isDeleted": false,
			"id": "imKoOw7t",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -133.54402822845373,
			"y": 62.941391774511544,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 200,
			"height": 25,
			"seed": 1431707113,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1736688394168,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "updateAnimations()",
			"rawText": "updateAnimations()",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "fzM2fBwrRhRaWiVdc6Uni",
			"originalText": "updateAnimations()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 420,
			"versionNonce": 493899655,
			"index": "aC",
			"isDeleted": false,
			"id": "rQk6UE52I7T2mZwch0osQ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -149.24110023762955,
			"y": 110.62075643230412,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 125.58750222860482,
			"height": 52.020891585574645,
			"seed": 1183611081,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "UV0Vp3Qp"
				},
				{
					"id": "ayez2O0CzrjBo4siH7r15",
					"type": "arrow"
				}
			],
			"updated": 1736690528387,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 449,
			"versionNonce": 60925863,
			"index": "aD",
			"isDeleted": false,
			"id": "UV0Vp3Qp",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -130.94734912332714,
			"y": 124.13120222509144,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 89,
			"height": 25,
			"seed": 972322729,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1736688394168,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "render()",
			"rawText": "render()",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "rQk6UE52I7T2mZwch0osQ",
			"originalText": "render()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 348,
			"versionNonce": 1625637130,
			"index": "aE",
			"isDeleted": false,
			"id": "41x7WAFFvkcwa0j1osffo",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -145.3126908785864,
			"y": -91.21135711572867,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 203.4571851630231,
			"height": 60,
			"seed": 1102682761,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "lHdvXDEE"
				},
				{
					"id": "mJmOc46pnfTrYpluVVecn",
					"type": "arrow"
				}
			],
			"updated": 1740462254225,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 388,
			"versionNonce": 735783399,
			"index": "aF",
			"isDeleted": false,
			"id": "lHdvXDEE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -121.58409829707486,
			"y": -73.71135711572867,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 156,
			"height": 25,
			"seed": 513237353,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1736688394168,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "handleEvents()",
			"rawText": "handleEvents()",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "41x7WAFFvkcwa0j1osffo",
			"originalText": "handleEvents()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 446,
			"versionNonce": 776762326,
			"index": "aG",
			"isDeleted": false,
			"id": "6wTYxwzNRo34w6oSadcCF",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -795.2260403643878,
			"y": 179.13548086023934,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 549.2320056553174,
			"height": 838.31371365696,
			"seed": 1399815593,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "ayez2O0CzrjBo4siH7r15",
					"type": "arrow"
				}
			],
			"updated": 1740463927816,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 288,
			"versionNonce": 882243158,
			"index": "aH",
			"isDeleted": false,
			"id": "o3vITPzs",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -766.9279979461984,
			"y": 196.5743231138,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 160.1999053955078,
			"height": 45,
			"seed": 1105453193,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740463927816,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 8,
			"text": "render()",
			"rawText": "render()",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "render()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1006,
			"versionNonce": 40942486,
			"index": "aM",
			"isDeleted": false,
			"id": "Cf4TGYH-j1POnSBG5KJJC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -774.1978610363676,
			"y": 715.298038511143,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 211.13277084472483,
			"height": 60,
			"seed": 1616472809,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "abwRj9k3"
				},
				{
					"id": "gqa4hXn-z29p_qMgCrL7Y",
					"type": "arrow"
				},
				{
					"id": "pyRCVaJkCnwbgem4omozW",
					"type": "arrow"
				},
				{
					"id": "89hUlBN2BUSknyicqJz9Y",
					"type": "arrow"
				}
			],
			"updated": 1740463927816,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1057,
			"versionNonce": 1799411926,
			"index": "aN",
			"isDeleted": false,
			"id": "abwRj9k3",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -762.1314756140052,
			"y": 732.798038511143,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 187,
			"height": 25,
			"seed": 228468169,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740463927816,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "switch(gameState)",
			"rawText": "switch(gameState)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Cf4TGYH-j1POnSBG5KJJC",
			"originalText": "switch(gameState)",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 452,
			"versionNonce": 163686291,
			"index": "aO",
			"isDeleted": false,
			"id": "ayez2O0CzrjBo4siH7r15",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -154.24110023762955,
			"y": 136.53120222509148,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 86.75293447144077,
			"height": 138.23317182489603,
			"seed": 983569447,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741671996193,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "rQk6UE52I7T2mZwch0osQ",
				"focus": 0.0038446092310996005,
				"gap": 5,
				"fixedPoint": [
					-0.039812878760010564,
					0.4980776953844502
				]
			},
			"endBinding": {
				"elementId": "6wTYxwzNRo34w6oSadcCF",
				"focus": -0.7718541600075037,
				"gap": 1,
				"fixedPoint": [
					1.0144927536231885,
					0.11407291999624823
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-43.37646723572044,
					0
				],
				[
					-43.37646723572044,
					138.23317182489603
				],
				[
					-86.75293447144077,
					138.23317182489603
				]
			],
			"elbowed": true
		},
		{
			"type": "rectangle",
			"version": 1202,
			"versionNonce": 1012579798,
			"index": "aP",
			"isDeleted": false,
			"id": "UWCjQi7FiWQuoqzwummfv",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -753.9880506761065,
			"y": 885.289430633007,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 168.2125462557874,
			"height": 85,
			"seed": 1858084039,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "J2CELgZF"
				},
				{
					"id": "gqa4hXn-z29p_qMgCrL7Y",
					"type": "arrow"
				},
				{
					"id": "X11qBGTE-hJE5Rz8Jqn_0",
					"type": "arrow"
				}
			],
			"updated": 1740463927817,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1295,
			"versionNonce": 1429246742,
			"index": "aQ",
			"isDeleted": false,
			"id": "J2CELgZF",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -747.8817775482128,
			"y": 890.289430633007,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 156,
			"height": 75,
			"seed": 1313795047,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740463927817,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "currentMenu\n->\nrender(window)",
			"rawText": "currentMenu\n->\nrender(window)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "UWCjQi7FiWQuoqzwummfv",
			"originalText": "currentMenu\n->\nrender(window)",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1110,
			"versionNonce": 584721110,
			"index": "aT",
			"isDeleted": false,
			"id": "qcISMEBqQolvApFsEcXJs",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -758.5963079248651,
			"y": 283.4846016175356,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 168.2125462557874,
			"height": 85,
			"seed": 221956615,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "P8vvrjyh"
				}
			],
			"updated": 1740463927817,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1221,
			"versionNonce": 1618696214,
			"index": "aU",
			"isDeleted": false,
			"id": "P8vvrjyh",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -752.4900347969714,
			"y": 288.4846016175356,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 156,
			"height": 75,
			"seed": 998371623,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740463927817,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "currentLevel\n->\nrender(window)",
			"rawText": "currentLevel\n->\nrender(window)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "qcISMEBqQolvApFsEcXJs",
			"originalText": "currentLevel\n->\nrender(window)",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1141,
			"versionNonce": 1455678806,
			"index": "aV",
			"isDeleted": false,
			"id": "8xfXxilc3wZUz6QtKLkPk",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -757.5471815324121,
			"y": 373.7094713684937,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 168.2125462557874,
			"height": 85,
			"seed": 1156945577,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "nc0KhXCW"
				}
			],
			"updated": 1740463927817,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1261,
			"versionNonce": 654887574,
			"index": "aW",
			"isDeleted": false,
			"id": "nc0KhXCW",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -751.4409084045184,
			"y": 378.7094713684937,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 156,
			"height": 75,
			"seed": 759093641,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740463927817,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "player\n->\nrender(window)",
			"rawText": "player\n->\nrender(window)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "8xfXxilc3wZUz6QtKLkPk",
			"originalText": "player\n->\nrender(window)",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 363,
			"versionNonce": 2147420118,
			"index": "aX",
			"isDeleted": false,
			"id": "5amtYERQDCoq2CM0xuJJm",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -769.9605365101947,
			"y": 267.23352364016733,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 195.13750899625882,
			"height": 304.0051735804723,
			"seed": 1183661929,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "pyRCVaJkCnwbgem4omozW",
					"type": "arrow"
				},
				{
					"id": "8PMaKCUEAT7IkQuBBGyfT",
					"type": "arrow"
				}
			],
			"updated": 1740463927817,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 578,
			"versionNonce": 63409075,
			"index": "aY",
			"isDeleted": false,
			"id": "gqa4hXn-z29p_qMgCrL7Y",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -668.7314756140053,
			"y": 780.298038511143,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1.2503019342075277,
			"height": 99.99139212186401,
			"seed": 734247369,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "FXUbHnxh"
				}
			],
			"updated": 1741671996197,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Cf4TGYH-j1POnSBG5KJJC",
				"focus": 0.0009472712322197163,
				"gap": 5,
				"fixedPoint": [
					0.4995263643838899,
					1.0833333333333333
				]
			},
			"endBinding": {
				"elementId": "UWCjQi7FiWQuoqzwummfv",
				"focus": -0.0011889719551353881,
				"gap": 5,
				"fixedPoint": [
					0.49940551402243233,
					-0.058823529411764705
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					49.995696060932005
				],
				[
					-1.2503019342075277,
					49.995696060932005
				],
				[
					-1.2503019342075277,
					99.99139212186401
				]
			],
			"elbowed": true
		},
		{
			"type": "text",
			"version": 12,
			"versionNonce": 21134919,
			"index": "aZ",
			"isDeleted": false,
			"id": "FXUbHnxh",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -701.7965908755426,
			"y": 816.793734572075,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 64.87992858886719,
			"height": 27,
			"seed": 1115649097,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1736690063537,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 6,
			"text": "default",
			"rawText": "default",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "gqa4hXn-z29p_qMgCrL7Y",
			"originalText": "default",
			"autoResize": true,
			"lineHeight": 1.35
		},
		{
			"type": "arrow",
			"version": 526,
			"versionNonce": 294636659,
			"index": "aa",
			"isDeleted": false,
			"id": "pyRCVaJkCnwbgem4omozW",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -668.7314756140053,
			"y": 710.298038511143,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 3.760306398060152,
			"height": 134.05934129050343,
			"seed": 835130279,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "fF2Q0HTq"
				}
			],
			"updated": 1741671996194,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Cf4TGYH-j1POnSBG5KJJC",
				"focus": -0.0009472712322197164,
				"gap": 5,
				"fixedPoint": [
					0.4995263643838899,
					-0.08333333333333333
				]
			},
			"endBinding": {
				"elementId": "5amtYERQDCoq2CM0xuJJm",
				"focus": 0.0010249182795712905,
				"gap": 5.000000000000028,
				"fixedPoint": [
					0.49948754086021463,
					1.0164470885186314
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					-67.02967064525171
				],
				[
					-3.760306398060152,
					-67.02967064525171
				],
				[
					-3.760306398060152,
					-134.05934129050343
				]
			],
			"elbowed": true
		},
		{
			"type": "text",
			"version": 10,
			"versionNonce": 1180606121,
			"index": "ab",
			"isDeleted": false,
			"id": "fF2Q0HTq",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -704.0315964644026,
			"y": 629.7683678658913,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 66.83993530273438,
			"height": 27,
			"seed": 1456572935,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1736690090628,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 6,
			"text": "playing",
			"rawText": "playing",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "pyRCVaJkCnwbgem4omozW",
			"originalText": "playing",
			"autoResize": true,
			"lineHeight": 1.35
		},
		{
			"type": "rectangle",
			"version": 375,
			"versionNonce": 1052495766,
			"index": "aj",
			"isDeleted": false,
			"id": "Y134ZxfVRmpwnxE2JwZo1",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -325.7602452218928,
			"y": 705.7616405930454,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 69.75258635247826,
			"height": 66.08139759708462,
			"seed": 820109767,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "89hUlBN2BUSknyicqJz9Y",
					"type": "arrow"
				},
				{
					"id": "8PMaKCUEAT7IkQuBBGyfT",
					"type": "arrow"
				},
				{
					"id": "X11qBGTE-hJE5Rz8Jqn_0",
					"type": "arrow"
				}
			],
			"updated": 1740463927817,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 597,
			"versionNonce": 1231275539,
			"index": "ak",
			"isDeleted": false,
			"id": "89hUlBN2BUSknyicqJz9Y",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -558.0650901916428,
			"y": 745.198038511143,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 227.30484496974998,
			"height": 6.495699119555184,
			"seed": 654977479,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "RdCG5fF5"
				}
			],
			"updated": 1741671996195,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Cf4TGYH-j1POnSBG5KJJC",
				"focus": -0.0033333333333340908,
				"gap": 5.000000000000057,
				"fixedPoint": [
					1.0236817808054877,
					0.49833333333333296
				]
			},
			"endBinding": {
				"elementId": "Y134ZxfVRmpwnxE2JwZo1",
				"focus": 0.0030265703703710577,
				"gap": 5,
				"fixedPoint": [
					-0.07168192982456131,
					0.49848671481481577
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					113.65242248487499,
					0
				],
				[
					113.65242248487499,
					-6.495699119555184
				],
				[
					227.30484496974998,
					-6.495699119555184
				]
			],
			"elbowed": true
		},
		{
			"type": "text",
			"version": 22,
			"versionNonce": 81789770,
			"index": "al",
			"isDeleted": false,
			"id": "RdCG5fF5",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -527.8025755436818,
			"y": 728.4501889513654,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 166.77981567382812,
			"height": 27,
			"seed": 270154695,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740463908903,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 6,
			"text": "pause / game over",
			"rawText": "pause / game over",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "89hUlBN2BUSknyicqJz9Y",
			"originalText": "pause / game over",
			"autoResize": true,
			"lineHeight": 1.35
		},
		{
			"type": "arrow",
			"version": 586,
			"versionNonce": 372913174,
			"index": "am",
			"isDeleted": false,
			"id": "8PMaKCUEAT7IkQuBBGyfT",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -290.98395204565367,
			"y": 700.7616405930454,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 278.83907546828226,
			"height": 281.67413007408936,
			"seed": 975497865,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "3oUFhdGC"
				}
			],
			"updated": 1740464237035,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Y134ZxfVRmpwnxE2JwZo1",
				"focus": -0.0028672771929831044,
				"gap": 5.000000000000057,
				"fixedPoint": [
					0.49856636140350846,
					-0.07566425925925922
				]
			},
			"endBinding": {
				"elementId": "5amtYERQDCoq2CM0xuJJm",
				"focus": -0.0009776143589743326,
				"gap": 4.999999999999943,
				"fixedPoint": [
					1.0256229569892472,
					0.49951119282051265
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					-281.67413007408936
				],
				[
					-278.83907546828226,
					-281.67413007408936
				]
			],
			"elbowed": true
		},
		{
			"type": "text",
			"version": 28,
			"versionNonce": 683884618,
			"index": "an",
			"isDeleted": false,
			"id": "3oUFhdGC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -321.33392763159117,
			"y": 378.58751051895604,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 60.699951171875,
			"height": 81,
			"seed": 685854953,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740464237036,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 6,
			"text": "render\nthis\nfirst",
			"rawText": "render\nthis\nfirst",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "8PMaKCUEAT7IkQuBBGyfT",
			"originalText": "render\nthis\nfirst",
			"autoResize": true,
			"lineHeight": 1.35
		},
		{
			"type": "arrow",
			"version": 596,
			"versionNonce": 1960942931,
			"index": "ao",
			"isDeleted": false,
			"id": "X11qBGTE-hJE5Rz8Jqn_0",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -290.98395204565367,
			"y": 776.8430381901301,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 289.7915523746654,
			"height": 150.8463924428769,
			"seed": 1940114985,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "jiyW48Gz"
				}
			],
			"updated": 1741671996197,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Y134ZxfVRmpwnxE2JwZo1",
				"focus": 0.0028672771929831044,
				"gap": 4.999999999999943,
				"fixedPoint": [
					0.49856636140350846,
					1.07566425925926
				]
			},
			"endBinding": {
				"elementId": "UWCjQi7FiWQuoqzwummfv",
				"focus": -0.002352941176471123,
				"gap": 5,
				"fixedPoint": [
					1.029724298878378,
					0.49882352941176444
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					150.8463924428769
				],
				[
					-289.7915523746654,
					150.8463924428769
				]
			],
			"elbowed": true
		},
		{
			"type": "text",
			"version": 34,
			"versionNonce": 1737332810,
			"index": "ap",
			"isDeleted": false,
			"id": "jiyW48Gz",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -321.33392763159117,
			"y": 887.189430633007,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 60.699951171875,
			"height": 81,
			"seed": 1323231593,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740464244630,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 6,
			"text": "then\nrender\nthis",
			"rawText": "then\nrender\nthis",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "X11qBGTE-hJE5Rz8Jqn_0",
			"originalText": "then\nrender\nthis",
			"autoResize": true,
			"lineHeight": 1.35
		},
		{
			"type": "rectangle",
			"version": 1158,
			"versionNonce": 1178883222,
			"index": "aq",
			"isDeleted": false,
			"id": "tWBFChH7w4h0ibQatbYLp",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -754.2406569732506,
			"y": 464.4802010469741,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 168.2125462557874,
			"height": 85,
			"seed": 1736231079,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "mD8LPOfn"
				}
			],
			"updated": 1740463927817,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1284,
			"versionNonce": 54088150,
			"index": "ar",
			"isDeleted": false,
			"id": "mD8LPOfn",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 0,
			"opacity": 100,
			"angle": 0,
			"x": -748.1343838453569,
			"y": 469.4802010469741,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 156,
			"height": 75,
			"seed": 105585607,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740463927817,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "GUI\n->\nrender(window)",
			"rawText": "GUI\n->\nrender(window)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "tWBFChH7w4h0ibQatbYLp",
			"originalText": "GUI\n->\nrender(window)",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1990,
			"versionNonce": 154982165,
			"index": "as",
			"isDeleted": false,
			"id": "Y7WcXsmN1h1lTnwIEneD1",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2058.4988526962456,
			"y": -415.96949230950634,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1206.925710893895,
			"height": 1002.9530277407615,
			"seed": 1094881159,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "mJmOc46pnfTrYpluVVecn",
					"type": "arrow"
				}
			],
			"updated": 1741409096184,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1263,
			"versionNonce": 1230766177,
			"index": "at",
			"isDeleted": false,
			"id": "NZIJlYUv",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2037.2646368107864,
			"y": -384.06699187383134,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 280.7998352050781,
			"height": 45,
			"seed": 1970603687,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328712690,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 8,
			"text": "handleEvents()",
			"rawText": "handleEvents()",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "handleEvents()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 1973,
			"versionNonce": 283983155,
			"index": "b02",
			"isDeleted": false,
			"id": "mJmOc46pnfTrYpluVVecn",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -150.3126908785864,
			"y": -70.61813509907256,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 696.2604509237642,
			"height": 196.52878539097162,
			"seed": 918752681,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741671996194,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "41x7WAFFvkcwa0j1osffo",
				"focus": 0.31355926611146284,
				"gap": 5,
				"fixedPoint": [
					-0.024575195002298274,
					0.34322036694426855
				]
			},
			"endBinding": {
				"elementId": "Y7WcXsmN1h1lTnwIEneD1",
				"focus": -0.7032312227927604,
				"gap": 5.414927619609878,
				"fixedPoint": [
					1.0144927536231885,
					0.1483843886036197
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-348.1302254618821,
					0
				],
				[
					-348.1302254618821,
					-196.52878539097162
				],
				[
					-696.2604509237642,
					-196.52878539097162
				]
			],
			"elbowed": true
		},
		{
			"type": "rectangle",
			"version": 1107,
			"versionNonce": 1998600623,
			"index": "b03",
			"isDeleted": false,
			"id": "QOL5JfsdBlvVaKiAc5rHj",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1759.6120523684667,
			"y": -302.86335614161897,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 213.52024090653268,
			"height": 60.34267677793308,
			"seed": 983138759,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "j6FWgYyx"
				},
				{
					"id": "mKKchcyJr-AGK9DTYJsl-",
					"type": "arrow"
				},
				{
					"id": "bCJTAcTCKZD50OPPU9dDi",
					"type": "arrow"
				},
				{
					"id": "fLKxYna2-A7yKS5loCkx0",
					"type": "arrow"
				}
			],
			"updated": 1741328704627,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1106,
			"versionNonce": 1342581851,
			"index": "b04",
			"isDeleted": false,
			"id": "j6FWgYyx",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1746.3519319152003,
			"y": -285.1920177526524,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 187,
			"height": 25,
			"seed": 798191207,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741408880709,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "switch(gameState)",
			"rawText": "switch(gameState)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "QOL5JfsdBlvVaKiAc5rHj",
			"originalText": "switch(gameState)",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1143,
			"versionNonce": 1270539343,
			"index": "b05",
			"isDeleted": false,
			"id": "fKsK8UGZvAISGJe-aVCg8",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1759.4634123192045,
			"y": -186.07307704848188,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 112.71682610395672,
			"height": 60.34267677793308,
			"seed": 1051392809,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "f4jdWPse"
				},
				{
					"id": "bCJTAcTCKZD50OPPU9dDi",
					"type": "arrow"
				},
				{
					"id": "9Fa4nrB_nRuFEmYIng5qO",
					"type": "arrow"
				}
			],
			"updated": 1741328444743,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1151,
			"versionNonce": 915898991,
			"index": "b06",
			"isDeleted": false,
			"id": "f4jdWPse",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1742.104999267226,
			"y": -168.40173865951533,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 78,
			"height": 25,
			"seed": 64204297,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328444743,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "playing",
			"rawText": "playing",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "fKsK8UGZvAISGJe-aVCg8",
			"originalText": "playing",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1588,
			"versionNonce": 757777615,
			"index": "b07",
			"isDeleted": false,
			"id": "RMZGGJXuRUaD7dsGNi75c",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1500.080297674479,
			"y": -187.1246493082266,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 120.82744568577326,
			"height": 60.34267677793308,
			"seed": 1855017929,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "jnfiiMnx"
				},
				{
					"id": "w7wnuyBkFRyiX_2fSkwj1",
					"type": "arrow"
				},
				{
					"id": "mKKchcyJr-AGK9DTYJsl-",
					"type": "arrow"
				}
			],
			"updated": 1741328444743,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1619,
			"versionNonce": 272061167,
			"index": "b08",
			"isDeleted": false,
			"id": "jnfiiMnx",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1478.1665748315922,
			"y": -169.45331091926005,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 77,
			"height": 25,
			"seed": 1655042729,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328444743,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "default",
			"rawText": "default",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "RMZGGJXuRUaD7dsGNi75c",
			"originalText": "default",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1866,
			"versionNonce": 1035431105,
			"index": "b09",
			"isDeleted": false,
			"id": "K8ptvzlfM-epo_UkOL9gI",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1246.3529562601816,
			"y": -87.82795777894057,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 334.48863614512237,
			"height": 49.56972908538114,
			"seed": 737390889,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "ZlIFeIn9"
				},
				{
					"id": "w7wnuyBkFRyiX_2fSkwj1",
					"type": "arrow"
				}
			],
			"updated": 1741328731588,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1905,
			"versionNonce": 546188449,
			"index": "b0A",
			"isDeleted": false,
			"id": "ZlIFeIn9",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1233.6086381876205,
			"y": -75.54309323625,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 309,
			"height": 25,
			"seed": 139969481,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328731588,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "currentMenu -> handleHover()",
			"rawText": "currentMenu -> handleHover()",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "K8ptvzlfM-epo_UkOL9gI",
			"originalText": "currentMenu -> handleHover()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 3833,
			"versionNonce": 1987986195,
			"index": "b0E",
			"isDeleted": false,
			"id": "w7wnuyBkFRyiX_2fSkwj1",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1374.2528519887057,
			"y": -157.05331091926007,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 300.5896206906373,
			"height": 54.505703640924025,
			"seed": 194709865,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741671996200,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "RMZGGJXuRUaD7dsGNi75c",
				"focus": -0.003314403846154603,
				"gap": 4.999999999999886,
				"fixedPoint": [
					1.04138132666483,
					0.49834279807692283
				]
			},
			"endBinding": {
				"elementId": "8e6ORi6Z_XpWW9enR__KE",
				"focus": -0.0009096821256048231,
				"gap": 1,
				"fixedPoint": [
					0.4995451589371979,
					-0.013978994320156235
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					300.5896206906373,
					0
				],
				[
					300.5896206906373,
					54.505703640924025
				]
			],
			"elbowed": true
		},
		{
			"type": "rectangle",
			"version": 1868,
			"versionNonce": 872062351,
			"index": "b0F",
			"isDeleted": false,
			"id": "XqVeTcrk6QMdP8olzE3sJ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -2009.0996513776972,
			"y": 222.58458976906468,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 213.52024090653268,
			"height": 85,
			"seed": 1916126919,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "HttWSyZF"
				},
				{
					"id": "9Fa4nrB_nRuFEmYIng5qO",
					"type": "arrow"
				},
				{
					"id": "kk-tVzMLhvFzHhv8LVCo-",
					"type": "arrow"
				}
			],
			"updated": 1741328444744,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1912,
			"versionNonce": 872279067,
			"index": "b0G",
			"isDeleted": false,
			"id": "HttWSyZF",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1996.8395309244308,
			"y": 227.58458976906468,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 189,
			"height": 75,
			"seed": 1769952743,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741408880717,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "player\n->\nhandleMovements()",
			"rawText": "player\n->\nhandleMovements()",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "XqVeTcrk6QMdP8olzE3sJ",
			"originalText": "player\n->\nhandleMovements()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 2576,
			"versionNonce": 666547443,
			"index": "b0H",
			"isDeleted": false,
			"id": "9Fa4nrB_nRuFEmYIng5qO",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1703.2049992672264,
			"y": -120.73040027054878,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 28.521711856597904,
			"height": 105.929383804917,
			"seed": 739058793,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741671996206,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "fKsK8UGZvAISGJe-aVCg8",
				"focus": 0.00177435798109034,
				"gap": 4.999999999999993,
				"fixedPoint": [
					0.4991128210094557,
					1.0828600961538464
				]
			},
			"endBinding": {
				"elementId": "o7U53uyY_npnO6wOSTdGO",
				"focus": -0.0017114811807538662,
				"gap": 3.489699843661768,
				"fixedPoint": [
					0.49914425940962354,
					-0.04005375366279373
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					52.964191852448494
				],
				[
					28.521711856597904,
					52.964191852448494
				],
				[
					28.521711856597904,
					105.929383804917
				]
			],
			"elbowed": true
		},
		{
			"type": "diamond",
			"version": 1632,
			"versionNonce": 1435644911,
			"index": "b0I",
			"isDeleted": false,
			"id": "XbhjghI9dmnqAKzEGWpn7",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1845.0209894488348,
			"y": 102.6345860338364,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 106.04147185562931,
			"height": 97.60635477620417,
			"seed": 1671417927,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "Nv7YLVQE"
				},
				{
					"id": "9Fa4nrB_nRuFEmYIng5qO",
					"type": "arrow"
				},
				{
					"id": "kk-tVzMLhvFzHhv8LVCo-",
					"type": "arrow"
				},
				{
					"id": "8QAOJsxEEmGpWNBEXZkg0",
					"type": "arrow"
				},
				{
					"id": "S9JxQ_avu9UsB7Bwbsh-P",
					"type": "arrow"
				}
			],
			"updated": 1741328444744,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1598,
			"versionNonce": 337894927,
			"index": "b0IV",
			"isDeleted": false,
			"id": "Nv7YLVQE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1809.0106214849275,
			"y": 139.03617472788744,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 34,
			"height": 25,
			"seed": 19327815,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328444744,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "esc",
			"rawText": "esc",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "XbhjghI9dmnqAKzEGWpn7",
			"originalText": "esc",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 3391,
			"versionNonce": 1333270515,
			"index": "b0K",
			"isDeleted": false,
			"id": "kk-tVzMLhvFzHhv8LVCo-",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1850.0199893488148,
			"y": 151.33776342193858,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 52.41954157561622,
			"height": 66.2468263471261,
			"seed": 338806953,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "x4uxmiig"
				}
			],
			"updated": 1741671996202,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "XbhjghI9dmnqAKzEGWpn7",
				"focus": 0.002049046913578386,
				"gap": 3.4590873309368533,
				"fixedPoint": [
					-0.0471419324204199,
					0.4989754765432108
				]
			},
			"endBinding": {
				"elementId": "XqVeTcrk6QMdP8olzE3sJ",
				"focus": -0.0009366793478273648,
				"gap": 5,
				"fixedPoint": [
					0.49953166032608654,
					-0.058823529411764705
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-52.41954157561622,
					0
				],
				[
					-52.41954157561622,
					66.2468263471261
				]
			],
			"elbowed": true
		},
		{
			"type": "text",
			"version": 6,
			"versionNonce": 820761345,
			"index": "b0L",
			"isDeleted": false,
			"id": "x4uxmiig",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1914.439530924431,
			"y": 138.83776342193858,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 24,
			"height": 25,
			"seed": 1660284711,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740027833405,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "no",
			"rawText": "no",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "kk-tVzMLhvFzHhv8LVCo-",
			"originalText": "no",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1991,
			"versionNonce": 2137579151,
			"index": "b0M",
			"isDeleted": false,
			"id": "JotI8MnCReEt6bXXXZh1N",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1748.4310060950324,
			"y": 211.77680973467818,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 257.5574829424806,
			"height": 85,
			"seed": 483001225,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "fu7seEmn"
				},
				{
					"id": "8QAOJsxEEmGpWNBEXZkg0",
					"type": "arrow"
				}
			],
			"updated": 1741328444744,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 2138,
			"versionNonce": 789329071,
			"index": "b0N",
			"isDeleted": false,
			"id": "fu7seEmn",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1740.6522646237922,
			"y": 241.77680973467818,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 242,
			"height": 25,
			"seed": 1840425577,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328444744,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "updateGameState(pause)",
			"rawText": "updateGameState(pause)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "JotI8MnCReEt6bXXXZh1N",
			"originalText": "updateGameState(pause)",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 3460,
			"versionNonce": 357800147,
			"index": "b0O",
			"isDeleted": false,
			"id": "8QAOJsxEEmGpWNBEXZkg0",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1733.9805176932255,
			"y": 151.33776342193858,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 114.20762868185784,
			"height": 55.439046312739606,
			"seed": 2143813225,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "VXmbNf5Z"
				}
			],
			"updated": 1741671996204,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "XbhjghI9dmnqAKzEGWpn7",
				"focus": -0.0020490469135783862,
				"gap": 3.4590873309368533,
				"fixedPoint": [
					1.047141932420421,
					0.4989754765432108
				]
			},
			"endBinding": {
				"elementId": "JotI8MnCReEt6bXXXZh1N",
				"focus": -0.0009366793478279837,
				"gap": 5,
				"fixedPoint": [
					0.4995316603260857,
					-0.058823529411764705
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					114.20762868185784,
					0
				],
				[
					114.20762868185784,
					55.439046312739606
				]
			],
			"elbowed": true
		},
		{
			"type": "text",
			"version": 7,
			"versionNonce": 45062543,
			"index": "b0P",
			"isDeleted": false,
			"id": "VXmbNf5Z",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1636.2728890113676,
			"y": 138.83776342193858,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 33,
			"height": 25,
			"seed": 944085257,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740027833405,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "yes",
			"rawText": "yes",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "8QAOJsxEEmGpWNBEXZkg0",
			"originalText": "yes",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 2270,
			"versionNonce": 42625203,
			"index": "b0Q",
			"isDeleted": false,
			"id": "mKKchcyJr-AGK9DTYJsl-",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1541.091811461934,
			"y": -272.79201775265244,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 101.32523663034158,
			"height": 80.66736844442585,
			"seed": 1893886535,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741671996201,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "QOL5JfsdBlvVaKiAc5rHj",
				"focus": -0.0033144038461546043,
				"gap": 5,
				"fixedPoint": [
					1.0234169836956526,
					0.49834279807692283
				]
			},
			"endBinding": {
				"elementId": "RMZGGJXuRUaD7dsGNi75c",
				"focus": -0.0016552530665954624,
				"gap": 5.000000000000007,
				"fixedPoint": [
					0.49917237346670307,
					-0.08286009615384625
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					101.32523663034158,
					0
				],
				[
					101.32523663034158,
					80.66736844442585
				]
			],
			"elbowed": true
		},
		{
			"type": "arrow",
			"version": 1921,
			"versionNonce": 1559944147,
			"index": "b0R",
			"isDeleted": false,
			"id": "bCJTAcTCKZD50OPPU9dDi",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1734.327600826026,
			"y": -237.52067936368587,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 25.411534846458835,
			"height": 46.447602315203994,
			"seed": 529333577,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741671996199,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "QOL5JfsdBlvVaKiAc5rHj",
				"focus": 0.7631657641908627,
				"gap": 5,
				"fixedPoint": [
					0.11841711790456882,
					1.0828600961538464
				]
			},
			"endBinding": {
				"elementId": "fKsK8UGZvAISGJe-aVCg8",
				"focus": -0.10310912599653174,
				"gap": 5.000000000000007,
				"fixedPoint": [
					0.448445437001735,
					-0.08286009615384625
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					23.223801157601997
				],
				[
					25.411534846458835,
					23.223801157601997
				],
				[
					25.411534846458835,
					46.447602315203994
				]
			],
			"elbowed": true
		},
		{
			"type": "rectangle",
			"version": 330,
			"versionNonce": 1385069718,
			"index": "b0S",
			"isDeleted": false,
			"id": "YV2AfMkdzZ-sqSMg3kJ1s",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -677.6862523650443,
			"y": 10.013301112049419,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 345,
			"height": 125.26136032459954,
			"seed": 543874281,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "kGTcvFTRtFb5w_mj4EaEY",
					"type": "arrow"
				}
			],
			"updated": 1740463927819,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 246,
			"versionNonce": 956092182,
			"index": "b0T",
			"isDeleted": false,
			"id": "XwTKZB1k",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -664.6862523650443,
			"y": 29.01330111204942,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 257.39984130859375,
			"height": 45,
			"seed": 1857116105,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740463927819,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 8,
			"text": "updateLogic()",
			"rawText": "updateLogic()",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "updateLogic()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 243,
			"versionNonce": 771652694,
			"index": "b0c",
			"isDeleted": false,
			"id": "YcZVNcYC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -661.6736078921938,
			"y": 87.21024731462956,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 142,
			"height": 25,
			"seed": 1775680711,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740463927819,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "TODO: Physics",
			"rawText": "TODO: Physics",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "TODO: Physics",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 279,
			"versionNonce": 342613491,
			"index": "b0d",
			"isDeleted": false,
			"id": "kGTcvFTRtFb5w_mj4EaEY",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -152.53129129167996,
			"y": 10.575276540228082,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 175.15496107336435,
			"height": 62.01340616389485,
			"seed": 2024459431,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741671996192,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "eibHsRJwwlAk6nfZVuTs7",
				"focus": 0.003440356862745311,
				"gap": 5,
				"fixedPoint": [
					-0.02829970967741933,
					0.4982798215686273
				]
			},
			"endBinding": {
				"elementId": "YV2AfMkdzZ-sqSMg3kJ1s",
				"focus": -0.0008829310185192288,
				"gap": 32,
				"fixedPoint": [
					1.0144927536231885,
					0.4995585344907404
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-87.57748053668217,
					0
				],
				[
					-87.57748053668217,
					62.01340616389485
				],
				[
					-175.15496107336435,
					62.01340616389485
				]
			],
			"elbowed": true
		},
		{
			"type": "rectangle",
			"version": 1237,
			"versionNonce": 1497109743,
			"index": "b0u",
			"isDeleted": false,
			"id": "9HzHn9gEUDIcZhMFF-udd",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1630.9333497761145,
			"y": -184.9801752894358,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 112.71682610395672,
			"height": 60.34267677793308,
			"seed": 861238354,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "jzhFQZ9R"
				},
				{
					"id": "fLKxYna2-A7yKS5loCkx0",
					"type": "arrow"
				},
				{
					"id": "MoUeJQrhTR1ZjBzDEQhk9",
					"type": "arrow"
				}
			],
			"updated": 1741328444745,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1252,
			"versionNonce": 703176463,
			"index": "b0v",
			"isDeleted": false,
			"id": "jzhFQZ9R",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1596.574936724136,
			"y": -167.30883690046926,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 44,
			"height": 25,
			"seed": 218569234,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328444745,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "quit",
			"rawText": "quit",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "9HzHn9gEUDIcZhMFF-udd",
			"originalText": "quit",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 1670,
			"versionNonce": 1336870515,
			"index": "b0w",
			"isDeleted": false,
			"id": "fLKxYna2-A7yKS5loCkx0",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1630.8159118137096,
			"y": -237.52067936368587,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 48.7899444276768,
			"height": 47.540504074250066,
			"seed": 1026267406,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741671996204,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "QOL5JfsdBlvVaKiAc5rHj",
				"focus": -0.20640684937346898,
				"gap": 5,
				"fixedPoint": [
					0.6032034246867347,
					1.0828600961538464
				]
			},
			"endBinding": {
				"elementId": "9HzHn9gEUDIcZhMFF-udd",
				"focus": -0.13220795722237266,
				"gap": 5.000000000000007,
				"fixedPoint": [
					0.43389602138881456,
					-0.08286009615384625
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					23.770252037125033
				],
				[
					48.7899444276768,
					23.770252037125033
				],
				[
					48.7899444276768,
					47.540504074250066
				]
			],
			"elbowed": true
		},
		{
			"type": "rectangle",
			"version": 1871,
			"versionNonce": 507637889,
			"index": "b0x",
			"isDeleted": false,
			"id": "78stfRriYn_glm6iLgJb7",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1239.9711411591197,
			"y": -28.547011854242328,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 321.0693748083627,
			"height": 85,
			"seed": 1807064801,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "uRSQttry"
				}
			],
			"updated": 1741328731588,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1967,
			"versionNonce": 1553086561,
			"index": "b0y",
			"isDeleted": false,
			"id": "uRSQttry",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1167.4364537549384,
			"y": -23.547011854242328,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 176,
			"height": 75,
			"seed": 1883314881,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328731588,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "trigger_data\n= currentMenu ->\nhandleTrigger()",
			"rawText": "trigger_data\n= currentMenu ->\nhandleTrigger()",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "78stfRriYn_glm6iLgJb7",
			"originalText": "trigger_data\n= currentMenu ->\nhandleTrigger()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1923,
			"versionNonce": 665935253,
			"index": "b0z",
			"isDeleted": false,
			"id": "8e6ORi6Z_XpWW9enR__KE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1257.5514612232942,
			"y": -97.54760727833605,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 368.1113241422561,
			"height": 663.2284596403354,
			"seed": 408014351,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "w7wnuyBkFRyiX_2fSkwj1",
					"type": "arrow"
				}
			],
			"updated": 1741409090869,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1006,
			"versionNonce": 1838753793,
			"index": "b19",
			"isDeleted": false,
			"id": "xEQofzOQ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1217.8587423208444,
			"y": 271.60065488147495,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 287,
			"height": 25,
			"seed": 624328417,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328731588,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "if (trigger_data.new_json)",
			"rawText": "if (trigger_data.new_json)",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "if (trigger_data.new_json)",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 2270,
			"versionNonce": 1405228277,
			"index": "b1A",
			"isDeleted": false,
			"id": "HCqI6TS2_J-e4NsqOSiXD",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1214.8783062755601,
			"y": 495.49966304204065,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 280.5374062719163,
			"height": 35,
			"seed": 256383105,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "WfFwsMHm"
				}
			],
			"updated": 1741409083853,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 2309,
			"versionNonce": 620605013,
			"index": "b1B",
			"isDeleted": false,
			"id": "WfFwsMHm",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1107.6096031396019,
			"y": 500.49966304204065,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 66,
			"height": 25,
			"seed": 445866081,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741409083853,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "save()",
			"rawText": "save()",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "HCqI6TS2_J-e4NsqOSiXD",
			"originalText": "save()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1133,
			"versionNonce": 42142427,
			"index": "b1C",
			"isDeleted": false,
			"id": "USprpeFqncU1HIKhbo7Mi",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1230.803323266309,
			"y": 258.64279633887134,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 314.26221911082956,
			"height": 291.1545250828193,
			"seed": 34290113,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1741409087786,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1227,
			"versionNonce": 299409281,
			"index": "b1D",
			"isDeleted": false,
			"id": "qLQAvmAk",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1229.2791359835167,
			"y": 78.17138014573425,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 297.0015134562475,
			"height": 50,
			"seed": 2141370671,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328731588,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "if (trigger_data.new_state\n        != currentState)",
			"rawText": "if (trigger_data.new_state\n        != currentState)",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "if (trigger_data.new_state\n        != currentState)",
			"autoResize": false,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 2321,
			"versionNonce": 662374241,
			"index": "b1E",
			"isDeleted": false,
			"id": "f5LxIX46dF-MaUz_pJRD8",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1224.9903072531756,
			"y": 139.68459576298307,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 291.59479911570935,
			"height": 87.02600442145435,
			"seed": 1282521935,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "B5u6EgYU"
				}
			],
			"updated": 1741328731588,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 2458,
			"versionNonce": 1346728769,
			"index": "b1F",
			"isDeleted": false,
			"id": "B5u6EgYU",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1211.6929076953209,
			"y": 158.19759797371023,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 265,
			"height": 50,
			"seed": 1213954415,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328731588,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "updateGameState\n(trigger_data.new_state)",
			"rawText": "updateGameState\n(trigger_data.new_state)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "f5LxIX46dF-MaUz_pJRD8",
			"originalText": "updateGameState\n(trigger_data.new_state)",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1230,
			"versionNonce": 1548919805,
			"index": "b1G",
			"isDeleted": false,
			"id": "5vGA0hEdYgUOdrIA91Ppn",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "dashed",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1246.4372025264843,
			"y": 62.744089672605355,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 327.2060021423356,
			"height": 180.7684354625045,
			"seed": 950563727,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1741671353091,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 2245,
			"versionNonce": 887117569,
			"index": "b1L",
			"isDeleted": false,
			"id": "Qz0cMz5Z67Ps3JoJ5gU_u",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1220.9423917431507,
			"y": 304.18939474993533,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 296.24930670951204,
			"height": 85,
			"seed": 1107690497,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "GbFeVUBV"
				}
			],
			"updated": 1741328731588,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 2389,
			"versionNonce": 1718470707,
			"index": "b1M",
			"isDeleted": false,
			"id": "GbFeVUBV",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1211.8177383883947,
			"y": 309.18939474993533,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 278,
			"height": 75,
			"seed": 629660641,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741672079195,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "settings =\ndifference_btwn(settings,\ntrigger_data.new_json)",
			"rawText": "settings = difference_btwn(settings, trigger_data.new_json)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Qz0cMz5Z67Ps3JoJ5gU_u",
			"originalText": "settings = difference_btwn(settings, trigger_data.new_json)",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "diamond",
			"version": 1530,
			"versionNonce": 825018479,
			"index": "b1U",
			"isDeleted": false,
			"id": "o7U53uyY_npnO6wOSTdGO",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1733.0122091685153,
			"y": -9.802016565651797,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 116.8578435157741,
			"height": 124.80727629339766,
			"seed": 670922698,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "BnOVqwSl"
				},
				{
					"id": "S9JxQ_avu9UsB7Bwbsh-P",
					"type": "arrow"
				},
				{
					"id": "yHnGUFkvoFSWfp0SH0HFy",
					"type": "arrow"
				},
				{
					"id": "9Fa4nrB_nRuFEmYIng5qO",
					"type": "arrow"
				}
			],
			"updated": 1741328444745,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1504,
			"versionNonce": 169933723,
			"index": "b1V",
			"isDeleted": false,
			"id": "BnOVqwSl",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1696.7977482895717,
			"y": 39.899802507697615,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 44,
			"height": 25,
			"seed": 1842343562,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741408880730,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "died",
			"rawText": "died",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "o7U53uyY_npnO6wOSTdGO",
			"originalText": "died",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 3249,
			"versionNonce": 450905523,
			"index": "b1W",
			"isDeleted": false,
			"id": "S9JxQ_avu9UsB7Bwbsh-P",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1738.0112090684952,
			"y": 52.50162158104706,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 54.08904445252483,
			"height": 45.133964552809346,
			"seed": 665161034,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "UdVm3dTi"
				}
			],
			"updated": 1741671996205,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "o7U53uyY_npnO6wOSTdGO",
				"focus": 0.001602470672701685,
				"gap": 3.7174767877610435,
				"fixedPoint": [
					-0.042778471256874964,
					0.49919876466364915
				]
			},
			"endBinding": {
				"elementId": "XbhjghI9dmnqAKzEGWpn7",
				"focus": -0.001886054545452831,
				"gap": 3.7458096756706425,
				"fixedPoint": [
					0.4990569727272741,
					-0.051215926580209896
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-54.08904445252483,
					0
				],
				[
					-54.08904445252483,
					45.133964552809346
				]
			],
			"elbowed": true
		},
		{
			"type": "text",
			"version": 9,
			"versionNonce": 1980894806,
			"index": "b1X",
			"isDeleted": false,
			"id": "UdVm3dTi",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1804.10025352102,
			"y": 40.00162158104706,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 24,
			"height": 25,
			"seed": 987321354,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740462213528,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "no",
			"rawText": "no",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "S9JxQ_avu9UsB7Bwbsh-P",
			"originalText": "no",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1867,
			"versionNonce": 827761423,
			"index": "b1Y",
			"isDeleted": false,
			"id": "BGqQRBFksZvqBtSqADhSL",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1564.1220797524838,
			"y": 108.68771073414678,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 290.80505262130623,
			"height": 85,
			"seed": 694567626,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "LibpxGbs"
				},
				{
					"id": "yHnGUFkvoFSWfp0SH0HFy",
					"type": "arrow"
				}
			],
			"updated": 1741328444745,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 2021,
			"versionNonce": 1473079599,
			"index": "b1Z",
			"isDeleted": false,
			"id": "LibpxGbs",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1556.2195534418306,
			"y": 138.68771073414678,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 275,
			"height": 25,
			"seed": 2112313738,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741328444745,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "updateGameState(GameOver)",
			"rawText": "updateGameState(GameOver)",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "BGqQRBFksZvqBtSqADhSL",
			"originalText": "updateGameState(GameOver)",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 3226,
			"versionNonce": 454925971,
			"index": "b1a",
			"isDeleted": false,
			"id": "yHnGUFkvoFSWfp0SH0HFy",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1611.156000942244,
			"y": 52.473753598906455,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 192.3002519568961,
			"height": 51.21395713524032,
			"seed": 932681802,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "Cw5A4CgU"
				}
			],
			"updated": 1741671996206,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "o7U53uyY_npnO6wOSTdGO",
				"focus": -0.002049046913578757,
				"gap": 3.7360602488945034,
				"fixedPoint": [
					1.0427730356826452,
					0.4989754765432106
				]
			},
			"endBinding": {
				"elementId": "BGqQRBFksZvqBtSqADhSL",
				"focus": -0.0009366793478283728,
				"gap": 5,
				"fixedPoint": [
					0.4995316603260862,
					-0.058823529411764705
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					192.3002519568961,
					0
				],
				[
					192.3002519568961,
					51.21395713524032
				]
			],
			"elbowed": true
		},
		{
			"type": "text",
			"version": 11,
			"versionNonce": 1747268438,
			"index": "b1b",
			"isDeleted": false,
			"id": "Cw5A4CgU",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1435.3557489853479,
			"y": 39.973753598906455,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 33,
			"height": 25,
			"seed": 911343370,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1740462213529,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "yes",
			"rawText": "yes",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "yHnGUFkvoFSWfp0SH0HFy",
			"originalText": "yes",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 1279,
			"versionNonce": 966404463,
			"index": "b1c",
			"isDeleted": false,
			"id": "Jgvr4uUV9RRMhE6OINURk",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1624.5176510399142,
			"y": -71.61466387374674,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 112.71682610395672,
			"height": 60.34267677793308,
			"seed": 1323234710,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "cKvrVDrv"
				},
				{
					"id": "MoUeJQrhTR1ZjBzDEQhk9",
					"type": "arrow"
				}
			],
			"updated": 1741328444746,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 1306,
			"versionNonce": 149175675,
			"index": "b1d",
			"isDeleted": false,
			"id": "cKvrVDrv",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1618.1592379879357,
			"y": -53.943325484780196,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 100,
			"height": 25,
			"seed": 1104663254,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741408880732,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "cleanup()",
			"rawText": "cleanup()",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Jgvr4uUV9RRMhE6OINURk",
			"originalText": "cleanup()",
			"autoResize": true,
			"lineHeight": 1.25
		},
		{
			"type": "arrow",
			"version": 911,
			"versionNonce": 565335091,
			"index": "b1e",
			"isDeleted": false,
			"id": "MoUeJQrhTR1ZjBzDEQhk9",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1574.6749367241362,
			"y": -119.63749851150271,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 6.415698736200284,
			"height": 43.02283463775598,
			"seed": 1156822678,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741671996207,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "9HzHn9gEUDIcZhMFF-udd",
				"focus": 0.001774357981086306,
				"gap": 4.999999999999993,
				"fixedPoint": [
					0.49911282100945775,
					1.0828600961538464
				]
			},
			"endBinding": {
				"elementId": "Jgvr4uUV9RRMhE6OINURk",
				"focus": -0.0017743579810863056,
				"gap": 5,
				"fixedPoint": [
					0.49911282100945775,
					-0.08286009615384625
				]
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					21.51141731887799
				],
				[
					6.415698736200284,
					21.51141731887799
				],
				[
					6.415698736200284,
					43.02283463775598
				]
			],
			"elbowed": true
		},
		{
			"type": "rectangle",
			"version": 2298,
			"versionNonce": 736212891,
			"index": "b1f",
			"isDeleted": false,
			"id": "AzcI_h0VAFpEmPxgh5HcL",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1222.0570184237536,
			"y": 400.09221173616817,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 296.24930670951204,
			"height": 85,
			"seed": 1416576315,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "oIuT29Fy"
				}
			],
			"updated": 1741409081336,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 2432,
			"versionNonce": 1805519931,
			"index": "b1g",
			"isDeleted": false,
			"id": "oIuT29Fy",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1162.4323650689976,
			"y": 430.09221173616817,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 177,
			"height": 25,
			"seed": 1604967899,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1741409081337,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 8,
			"text": "updateSettings()",
			"rawText": "updateSettings()",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "AzcI_h0VAFpEmPxgh5HcL",
			"originalText": "updateSettings()",
			"autoResize": true,
			"lineHeight": 1.25
		}
	],
	"appState": {
		"theme": "dark",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 2,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 8,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"currentItemArrowType": "elbow",
		"scrollX": 1675.3969401030313,
		"scrollY": 127.68704823587859,
		"zoom": {
			"value": 0.929647
		},
		"currentItemRoundness": "round",
		"gridSize": 20,
		"gridStep": 5,
		"gridModeEnabled": false,
		"gridColor": {
			"Bold": "rgba(217, 217, 217, 0.5)",
			"Regular": "rgba(230, 230, 230, 0.5)"
		},
		"currentStrokeOptions": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		},
		"objectsSnapModeEnabled": false,
		"activeTool": {
			"type": "selection",
			"customType": null,
			"locked": false,
			"lastActiveTool": null
		}
	},
	"files": {}
}
```
%%