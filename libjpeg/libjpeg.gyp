{
	'includes':
	[
		'../../common.gypi',
	],
	
	'targets':
	[
		{
			'target_name': 'libjpeg',

			'toolsets': ['host', 'target'],
			
			'conditions':
			[
				[
					'use_system_libjpeg == 0',
					{
						'type': 'static_library',
						
						'variables':
						{
							'silence_warnings': 1,
						},
						
						'defines':
						[
							'HAVE_STDLIB_H',
						],

						'include_dirs':
						[
							'src',
						],
						
						'sources':
						[
							'src/cderror.h',
							'src/cdjpeg.h',
							'src/jchuff.h',
							#'src/jconfig.h',
							'src/jdct.h',
							'src/jdhuff.h',
							'src/jerror.h',
							'src/jinclude.h',
							'src/jmemsys.h',
							'src/jmorecfg.h',
							'src/jpegint.h',
							'src/jpeglib.h',
							'src/jversion.h',
							'src/transupp.h',
							
							'src/ansi2knr.c',
							'src/cdjpeg.c',
							'src/cjpeg.c',
							'src/djpeg.c',
							'src/jcapimin.c',

							'src/jcapistd.c',
							'src/jccoefct.c',
							'src/jccolor.c',
							'src/jcdctmgr.c',
							'src/jchuff.c',
							'src/jcinit.c',
							'src/jcmainct.c',
							'src/jcmarker.c',
							'src/jcmaster.c',
							'src/jcomapi.c',
							'src/jcparam.c',
							'src/jcphuff.c',
							'src/jcprepct.c',
							'src/jcsample.c',

							'src/jctrans.c',
							'src/jdapimin.c',
							'src/jdapistd.c',
							'src/jdatadst.c',
							'src/jdatasrc.c',
							'src/jdcoefct.c',
							'src/jdcolor.c',

							'src/jddctmgr.c',
							'src/jdhuff.c',
							'src/jdinput.c',
							'src/jdmainct.c',
							'src/jdmarker.c',
							'src/jdmaster.c',
							'src/jdmerge.c',

							'src/jdphuff.c',
							'src/jdpostct.c',
							'src/jdsample.c',
							'src/jdtrans.c',
							'src/jerror.c',
							'src/jfdctflt.c',
							'src/jfdctfst.c',

							'src/jfdctint.c',
							'src/jidctflt.c',
							'src/jidctfst.c',
							'src/jidctint.c',
							'src/jidctred.c',
							'src/jmemansi.c',

							'src/jmemmgr.c',
							'src/jmemname.c',
							'src/jmemnobs.c',
							'src/jpegtran.c',
							'src/jquant1.c',
							'src/jquant2.c',

							'src/jutils.c',
							'src/rdbmp.c',
							'src/rdcolmap.c',
							'src/rdgif.c',
							'src/rdjpgcom.c',
							'src/rdppm.c',
							'src/rdrle.c',

							'src/rdswitch.c',
							'src/rdtarga.c',
							'src/transupp.c',
							'src/wrbmp.c',
							'src/wrgif.c',
							'src/wrjpgcom.c',
							'src/wrppm.c',

							'src/wrrle.c',
							'src/wrtarga.c',
						],
						
						'conditions':
						[
							[
								'OS == "win"',
								{
									'defines':
									[
										'USE_MSDOS_MEMMGR',
									],
									
									'sources/':
									[
										'src/jmemdos.c',
									],
								},
							],
							[
								'OS == "mac"',
								{
									'defines':
									[
										'USE_MAC_MEMMGR',
									],
									
									'sources/':
									[
										'src/jmemmac.c',
									],
								},
							],
						],

						'direct_dependent_settings':
						{
							'include_dirs':
							[
								'include',
							],
						},
					},
					{
						'type': 'none',
						
						'link_settings':
						{
							'libraries':
							[
								'-ljpeg',
							],
						},
					},
				],
			],
		},
	],
}
