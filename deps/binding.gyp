{
	"target_defaults" : {
		"default_configuration" : "Debug",
		"configuration" : {
			"Debug" : {
				"defines" : ["DEBUG", "_DEBUG"]
			},
			"Release" : {
				"defines" : ["NODEBUG"]
			}
		}
	},
	"targets" : [
		{
			"target_name" : "espeak",
			"type" : "static_library",
			"cflags" : [
				"-Wall",
				"-Wno-unused-parameter",
				"-Wno-missing-field-initializers",
				"-Wextra",
				"-Wno-narrowing"
			],
			"include_dirs": [
				"<!(node -e \"require('nan')\")"
			],
			"sources" : [
				#"espeak/src/compiledata.cpp",
				"espeak/src/espeak-ng.c",
				"espeak/src/speak-ng.c"
			]
		}
	]
}
