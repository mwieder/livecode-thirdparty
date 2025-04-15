{
	'includes':
	[
		'../../common.gypi',
	],

	'targets':
	[
		{
			'target_name': 'libpng',

			'toolsets': ['host', 'target'],

			'dependencies':
			[
				'../libz/libz.gyp:libz',
			],

			'conditions':
			[
				[
					'use_system_libpng == 0',
					{
						'type': 'static_library',

						'variables':
						{
							'silence_warnings': 1,
						},

						'include_dirs':
						[
							'src',
						],

						'sources':
						[
							'src/png.h',
							'src/pngconf.h',
							'src/pngdebug.h',
							'src/pnginfo.h',
							'src/pnglibconf.h',
							'src/pngstruct.h',

#							'src/pngpriv.h',
							'src/png.c',
							'src/pngerror.c',
							'src/pngget.c',
							'src/pngmem.c',
							'src/pngpread.c',
							'src/pngread.c',
							'src/pngrio.c',
							'src/pngrtran.c',
							'src/pngrutil.c',
							'src/pngset.c',
							'src/pngtrans.c',
							'src/pngwio.c',
							'src/pngwrite.c',
							'src/pngwtran.c',
							'src/pngwutil.c',
						],


                        'defines':
                        [
				'PNG_ARM_NEON_OPT=0',
                        ],
				},
					{
						'type': 'none',

						'link_settings':
						{
							'libraries':
							[
								'-lpng',
							],
						},
					},
				],
			],
		},
	],
}
