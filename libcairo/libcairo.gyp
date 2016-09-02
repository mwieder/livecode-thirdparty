{
	'includes':
	[
		'../../common.gypi',
	],
	
	'targets':
	[
		{
			'target_name': 'libcairo',
			
			'variables':
			{
				'library_for_module': 1,
				'silence_warnings': 1,
			},
			
			'conditions':
			[
				[
					'use_system_libcairo == 0',
					{
						'type': 'static_library',
						
						'dependencies':
						[
							'../libz/libz.gyp:libz',
						],
						
						'include_dirs':
						[
							'src',
						],
						
						'sources':
						[
							'src/cairo-analysis-surface-private.h',
							'src/cairo-arc-private.h',
							'src/cairo-array-private.h',
							'src/cairo-atomic-private.h',
							'src/cairo-backend-private.h',
							'src/cairo-beos.h',
							'src/cairo-box-inline.h',
							'src/cairo-boxes-private.h',
							'src/cairo-cache-private.h',
							'src/cairo-clip-inline.h',
							'src/cairo-clip-private.h',
							'src/cairo-cogl-context-private.h',
							'src/cairo-cogl-gradient-private.h',
							'src/cairo-cogl-private.h',
							'src/cairo-cogl-utils-private.h',
							'src/cairo-cogl.h',
							'src/cairo-combsort-inline.h',
							'src/cairo-compiler-private.h',
							'src/cairo-composite-rectangles-private.h',
							'src/cairo-compositor-private.h',
							'src/cairo-contour-inline.h',
							'src/cairo-contour-private.h',
							'src/cairo-damage-private.h',
							'src/cairo-default-context-private.h',
							'src/cairo-deprecated.h',
							'src/cairo-device-private.h',
							'src/cairo-directfb.h',
							'src/cairo-drm-i915-private.h',
							'src/cairo-drm-i965-private.h',
							'src/cairo-drm-intel-brw-defines.h',
							'src/cairo-drm-intel-brw-eu.h',
							'src/cairo-drm-intel-brw-structs.h',
							'src/cairo-drm-intel-command-private.h',
							'src/cairo-drm-intel-ioctl-private.h',
							'src/cairo-drm-intel-private.h',
							'src/cairo-drm-ioctl-private.h',
							'src/cairo-drm-private.h',
							'src/cairo-drm-radeon-private.h',
							'src/cairo-drm.h',
							'src/cairo-error-inline.h',
							'src/cairo-error-private.h',
							'src/cairo-features.h',
							'src/cairo-fixed-private.h',
							'src/cairo-fixed-type-private.h',
							'src/cairo-fontconfig-private.h',
							'src/cairo-freed-pool-private.h',
							'src/cairo-freelist-private.h',
							'src/cairo-freelist-type-private.h',
							'src/cairo-ft-private.h',
							'src/cairo-ft.h',
							'src/cairo-gl-dispatch-private.h',
							'src/cairo-gl-ext-def-private.h',
							'src/cairo-gl-gradient-private.h',
							'src/cairo-gl-private.h',
							'src/cairo-gl.h',
							'src/cairo-gstate-private.h',
							'src/cairo-hash-private.h',
							'src/cairo-image-info-private.h',
							'src/cairo-image-surface-inline.h',
							'src/cairo-image-surface-private.h',
							'src/cairo-line-inline.h',
							'src/cairo-line-private.h',
							'src/cairo-list-inline.h',
							'src/cairo-list-private.h',
							'src/cairo-malloc-private.h',
							'src/cairo-mempool-private.h',
							'src/cairo-mutex-impl-private.h',
							'src/cairo-mutex-list-private.h',
							'src/cairo-mutex-private.h',
							'src/cairo-mutex-type-private.h',
							'src/cairo-os2-private.h',
							'src/cairo-os2.h',
							'src/cairo-output-stream-private.h',
							'src/cairo-paginated-private.h',
							'src/cairo-paginated-surface-private.h',
							'src/cairo-path-fixed-private.h',
							'src/cairo-path-private.h',
							'src/cairo-pattern-inline.h',
							'src/cairo-pattern-private.h',
							'src/cairo-pdf-operators-private.h',
							'src/cairo-pdf-shading-private.h',
							'src/cairo-pdf-surface-private.h',
							'src/cairo-pdf.h',
							'src/cairo-pixman-private.h',
							'src/cairo-private.h',
							'src/cairo-ps-surface-private.h',
							'src/cairo-ps.h',
							'src/cairo-qt.h',
							'src/cairo-quartz-image.h',
							'src/cairo-quartz-private.h',
							'src/cairo-quartz.h',
							'src/cairo-recording-surface-inline.h',
							'src/cairo-recording-surface-private.h',
							'src/cairo-reference-count-private.h',
							'src/cairo-region-private.h',
							'src/cairo-rtree-private.h',
							'src/cairo-scaled-font-private.h',
							'src/cairo-scaled-font-subsets-private.h',
							'src/cairo-script-private.h',
							'src/cairo-script.h',
							'src/cairo-skia-private.h',
							'src/cairo-skia.h',
							'src/cairo-slope-private.h',
							'src/cairo-spans-compositor-private.h',
							'src/cairo-spans-private.h',
							'src/cairo-stroke-dash-private.h',
							'src/cairo-surface-backend-private.h',
							'src/cairo-surface-clipper-private.h',
							'src/cairo-surface-fallback-private.h',
							'src/cairo-surface-inline.h',
							'src/cairo-surface-observer-inline.h',
							'src/cairo-surface-observer-private.h',
							'src/cairo-surface-offset-private.h',
							'src/cairo-surface-private.h',
							'src/cairo-surface-snapshot-inline.h',
							'src/cairo-surface-snapshot-private.h',
							'src/cairo-surface-subsurface-inline.h',
							'src/cairo-surface-subsurface-private.h',
							'src/cairo-surface-wrapper-private.h',
							'src/cairo-svg-surface-private.h',
							'src/cairo-svg.h',
							'src/cairo-tee-surface-private.h',
							'src/cairo-tee.h',
							'src/cairo-time-private.h',
							'src/cairo-traps-private.h',
							'src/cairo-tristrip-private.h',
							'src/cairo-truetype-subset-private.h',
							'src/cairo-type1-private.h',
							'src/cairo-type3-glyph-surface-private.h',
							'src/cairo-types-private.h',
							'src/cairo-user-font-private.h',
							'src/cairo-version.h',
							'src/cairo-vg.h',
							'src/cairo-wideint-private.h',
							'src/cairo-wideint-type-private.h',
							'src/cairo-win32-private.h',
							'src/cairo-win32.h',
							'src/cairo-xcb-private.h',
							'src/cairo-xcb.h',
							'src/cairo-xlib-private.h',
							'src/cairo-xlib-surface-private.h',
							'src/cairo-xlib-xrender-private.h',
							'src/cairo-xlib-xrender.h',
							'src/cairo-xlib.h',
							'src/cairo-xml.h',
							'src/cairo.h',
							'src/cairoint.h',

							'src/pixman-accessor.h',
							'src/pixman-arm-asm.h',
							'src/pixman-arm-common.h',
							'src/pixman-arm-neon-asm.h',
							'src/pixman-arm-simd-asm.h',
							'src/pixman-combine32.h',
							'src/pixman-compiler.h',
							'src/pixman-config.h',
							'src/pixman-edge-imp.h',
							'src/pixman-inlines.h',
							'src/pixman-mips-dspr2-asm.h',
							'src/pixman-mips-dspr2.h',
							'src/pixman-private.h',
							'src/pixman-version.h',
							'src/pixman.h',
							
							'src/cairo-analysis-surface.c',
							'src/cairo-arc.c',
							'src/cairo-array.c',
							'src/cairo-atomic.c',
							'src/cairo-base64-stream.c',
							'src/cairo-base85-stream.c',
							'src/cairo-bentley-ottmann-rectangular.c',
							'src/cairo-bentley-ottmann-rectilinear.c',
							'src/cairo-bentley-ottmann.c',
							'src/cairo-botor-scan-converter.c',
							'src/cairo-boxes-intersect.c',
							'src/cairo-boxes.c',
							'src/cairo-cache.c',
							'src/cairo-cff-subset.c',
							'src/cairo-clip-boxes.c',
							'src/cairo-clip-polygon.c',
							'src/cairo-clip-region.c',
							'src/cairo-clip-surface.c',
							'src/cairo-clip-tor-scan-converter.c',
							'src/cairo-clip.c',
							'src/cairo-cogl-context.c',
							'src/cairo-cogl-gradient.c',
							'src/cairo-cogl-surface.c',
							'src/cairo-cogl-utils.c',
							'src/cairo-color.c',
							'src/cairo-composite-rectangles.c',
							'src/cairo-compositor.c',
							'src/cairo-contour.c',
							'src/cairo-damage.c',
							'src/cairo-debug.c',
							'src/cairo-default-context.c',
							'src/cairo-deflate-stream.c',
							'src/cairo-device.c',
							'src/cairo-directfb-surface.c',
							'src/cairo-drm-bo.c',
							'src/cairo-drm-gallium-surface.c',
							'src/cairo-drm-i915-glyphs.c',
							'src/cairo-drm-i915-shader.c',
							'src/cairo-drm-i915-spans.c',
							'src/cairo-drm-i915-surface.c',
							'src/cairo-drm-i965-glyphs.c',
							'src/cairo-drm-i965-shader.c',
							'src/cairo-drm-i965-spans.c',
							'src/cairo-drm-i965-surface.c',
							'src/cairo-drm-intel-brw-eu-emit.c',
							'src/cairo-drm-intel-brw-eu-util.c',
							'src/cairo-drm-intel-brw-eu.c',
							'src/cairo-drm-intel-debug.c',
							'src/cairo-drm-intel-surface.c',
							'src/cairo-drm-intel.c',
							'src/cairo-drm-radeon-surface.c',
							'src/cairo-drm-radeon.c',
							'src/cairo-drm-surface.c',
							'src/cairo-drm.c',
							'src/cairo-egl-context.c',
							'src/cairo-error.c',
							'src/cairo-fallback-compositor.c',
							'src/cairo-fixed.c',
							'src/cairo-font-face-twin-data.c',
							'src/cairo-font-face-twin.c',
							'src/cairo-font-face.c',
							'src/cairo-font-options.c',
							'src/cairo-freed-pool.c',
							'src/cairo-freelist.c',
							'src/cairo-ft-font.c',
							'src/cairo-gl-composite.c',
							'src/cairo-gl-device.c',
							'src/cairo-gl-dispatch.c',
							'src/cairo-gl-glyphs.c',
							'src/cairo-gl-gradient.c',
							'src/cairo-gl-info.c',
							'src/cairo-gl-msaa-compositor.c',
							'src/cairo-gl-operand.c',
							'src/cairo-gl-shaders.c',
							'src/cairo-gl-source.c',
							'src/cairo-gl-spans-compositor.c',
							'src/cairo-gl-surface.c',
							'src/cairo-gl-traps-compositor.c',
							'src/cairo-glx-context.c',
							'src/cairo-gstate.c',
							'src/cairo-hash.c',
							'src/cairo-hull.c',
							'src/cairo-image-compositor.c',
							'src/cairo-image-info.c',
							'src/cairo-image-source.c',
							'src/cairo-image-surface.c',
							'src/cairo-line.c',
							'src/cairo-lzw.c',
							'src/cairo-mask-compositor.c',
							'src/cairo-matrix.c',
							'src/cairo-mempool.c',
							'src/cairo-mesh-pattern-rasterizer.c',
							'src/cairo-misc.c',
							'src/cairo-mono-scan-converter.c',
							'src/cairo-mutex.c',
							'src/cairo-no-compositor.c',
							'src/cairo-observer.c',
							'src/cairo-os2-surface.c',
							'src/cairo-output-stream.c',
							'src/cairo-paginated-surface.c',
							'src/cairo-path-bounds.c',
							'src/cairo-path-fill.c',
							'src/cairo-path-fixed.c',
							'src/cairo-path-in-fill.c',
							'src/cairo-path-stroke-boxes.c',
							'src/cairo-path-stroke-polygon.c',
							'src/cairo-path-stroke-traps.c',
							'src/cairo-path-stroke-tristrip.c',
							'src/cairo-path-stroke.c',
							'src/cairo-path.c',
							'src/cairo-pattern.c',
							'src/cairo-pdf-operators.c',
							'src/cairo-pdf-shading.c',
							'src/cairo-pdf-surface.c',
							'src/cairo-pen.c',
							'src/cairo-png.c',
							'src/cairo-polygon-intersect.c',
							'src/cairo-polygon-reduce.c',
							'src/cairo-polygon.c',
							'src/cairo-ps-surface.c',
							'src/cairo-quartz-font.c',
							'src/cairo-quartz-image-surface.c',
							'src/cairo-quartz-surface.c',
							'src/cairo-raster-source-pattern.c',
							'src/cairo-recording-surface.c',
							'src/cairo-rectangle.c',
							'src/cairo-rectangular-scan-converter.c',
							'src/cairo-region.c',
							'src/cairo-rtree.c',
							'src/cairo-scaled-font-subsets.c',
							'src/cairo-scaled-font.c',
							'src/cairo-script-surface.c',
							'src/cairo-shape-mask-compositor.c',
							'src/cairo-slope.c',
							'src/cairo-spans-compositor.c',
							'src/cairo-spans.c',
							'src/cairo-spline.c',
							'src/cairo-stroke-dash.c',
							'src/cairo-stroke-style.c',
							'src/cairo-surface-clipper.c',
							'src/cairo-surface-fallback.c',
							'src/cairo-surface-observer.c',
							'src/cairo-surface-offset.c',
							'src/cairo-surface-snapshot.c',
							'src/cairo-surface-subsurface.c',
							'src/cairo-surface-wrapper.c',
							'src/cairo-surface.c',
							'src/cairo-svg-surface.c',
							'src/cairo-tee-surface.c',
							'src/cairo-time.c',
							'src/cairo-tor-scan-converter.c',
							'src/cairo-tor22-scan-converter.c',
							'src/cairo-toy-font-face.c',
							'src/cairo-traps-compositor.c',
							'src/cairo-traps.c',
							'src/cairo-tristrip.c',
							'src/cairo-truetype-subset.c',
							'src/cairo-type1-fallback.c',
							'src/cairo-type1-glyph-names.c',
							'src/cairo-type1-subset.c',
							'src/cairo-type3-glyph-surface.c',
							'src/cairo-unicode.c',
							'src/cairo-user-font.c',
							'src/cairo-version.c',
							'src/cairo-vg-surface.c',
							'src/cairo-wgl-context.c',
							'src/cairo-wideint.c',
							'src/cairo-win32-debug.c',
							'src/cairo-win32-device.c',
							'src/cairo-win32-display-surface.c',
							'src/cairo-win32-font.c',
							'src/cairo-win32-gdi-compositor.c',
							'src/cairo-win32-printing-surface.c',
							'src/cairo-win32-surface.c',
							'src/cairo-win32-system.c',
							'src/cairo-xcb-connection-core.c',
							'src/cairo-xcb-connection-render.c',
							'src/cairo-xcb-connection-shm.c',
							'src/cairo-xcb-connection.c',
							'src/cairo-xcb-resources.c',
							'src/cairo-xcb-screen.c',
							'src/cairo-xcb-shm.c',
							'src/cairo-xcb-surface-core.c',
							'src/cairo-xcb-surface-render.c',
							'src/cairo-xcb-surface.c',
							'src/cairo-xlib-core-compositor.c',
							'src/cairo-xlib-display.c',
							'src/cairo-xlib-fallback-compositor.c',
							'src/cairo-xlib-render-compositor.c',
							'src/cairo-xlib-screen.c',
							'src/cairo-xlib-source.c',
							'src/cairo-xlib-surface-shm.c',
							'src/cairo-xlib-surface.c',
							'src/cairo-xlib-visual.c',
							'src/cairo-xlib-xcb-surface.c',
							'src/cairo-xml-surface.c',
							'src/cairo.c',
							
							'src/pixman-access-accessors.c',
							'src/pixman-access.c',
							'src/pixman-arm-neon.c',
							'src/pixman-arm-simd.c',
							'src/pixman-arm.c',
							'src/pixman-bits-image.c',
							'src/pixman-combine-float.c',
							'src/pixman-combine32.c',
							'src/pixman-conical-gradient.c',
							'src/pixman-edge-accessors.c',
							'src/pixman-edge.c',
							'src/pixman-fast-path.c',
							'src/pixman-filter.c',
							'src/pixman-general.c',
							'src/pixman-glyph.c',
							'src/pixman-gradient-walker.c',
							'src/pixman-image.c',
							'src/pixman-implementation.c',
							'src/pixman-linear-gradient.c',
							'src/pixman-matrix.c',
							'src/pixman-mips-dspr2.c',
							'src/pixman-mips.c',
							'src/pixman-mmx.c',
							'src/pixman-noop.c',
							'src/pixman-ppc.c',
							'src/pixman-radial-gradient.c',
							'src/pixman-region.c',
							'src/pixman-region16.c',
							'src/pixman-region32.c',
							'src/pixman-solid-fill.c',
							'src/pixman-sse2.c',
							'src/pixman-ssse3.c',
							'src/pixman-timer.c',
							'src/pixman-trap.c',
							'src/pixman-utils.c',
							'src/pixman-vmx.c',
							'src/pixman-x86.c',
							'src/pixman.c',
						],
						
						# Cairo has a lot of backends and features that we don't need
						'sources/':
						[
							['exclude', '^src/cairo-(wgl|tee|egl|gl|directfb|eagle|ft|os2|png|ps|qt|quartz|skia|script|svg|vg|win32|xcb|xlib|xml|cogl|drm).*\\.c(pp)?$'],
							['exclude', '^src/pixman-(vmx).*\\.c$'],
						],
						
						# These files don't compile and aren't needed, seemingly
						'sources!':
						[
							'src/pixman-region.c',
						],
						
						'conditions':
						[
							[
								# Not supported on Android
								'OS == "android" or OS == "emscripten"',
								{
									'type': 'none',
								},
							],
							[
								# Re-add the OSX- and iOS-specific support
								'OS == "mac" or OS == "ios"',
								{
									'sources/':
									[
										['include', '^src/cairo-quartz.*\\.c$'],
										['exclude', '^src/cairo-quartz-image.*\\.c$'],
									],
									
									'link_settings':
									{
										'libraries':
										[
											'$(SDKROOT)/System/Library/Frameworks/ApplicationServices.framework',
											'$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework',
										],
									},
								},
							],
							[
								# SSE2 optimisations are restricted to OSX or x86_64
								'OS != "mac"',
								{
									'sources/':
									[
										['exclude', '-sse2\\.c$'],
									],
								},
							],
							[
								# Use the FreeType support on Linux
								'OS == "linux"',
								{
									'sources/':
									[
										['include', '^src/cairo-ft.*\\.c$'],
									],
								},
							],
							[
								# Re-add the windows-specific support
								'OS == "win"',
								{
									'sources/':
									[
										['include', '-win32-'],
									],
									
									'link_settings':
									{
										'libraries':
										[
											'-lgdi32',
											'-luser32',
											'-lmsimg32',
										],
									},
								},
							],
						],
						
						'direct_dependent_settings':
						{
							'include_dirs':
							[
								'src',
							],
						},
					},
					{
						'type': 'none',
						
						'link_settings':
						{
							'libraries':
							[
								'-lcairo',
							],
						},
					},
				],
			],
		},
	],
}
