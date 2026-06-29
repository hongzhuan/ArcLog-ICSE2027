# Ground Truth for zstd-v1.5.5-v1.5.6

## Important Changes

### Advanced Features

- [GT-ZSTD-v1.5.6-0010] lib: fix zdict prototype mismatch in static_only mode, by @ldv-alt (PRs: #3733; commits: ecb86d8)
- [GT-ZSTD-v1.5.6-0028] port: QNX support by @klausholstjacobsen (PRs: #3745; commits: 839c793)
- [GT-ZSTD-v1.5.6-0036] Added ZSTD_CCtxParams_registerSequenceProducer public API to enable external sequence generators to be used with static CCtx. (Architecture event: Zstd_Core_Module module change) (PRs: #3854; commits: c6cabf9)
- [GT-ZSTD-v1.5.6-0039] Enable utimensat support on FreeBSD, using more precise timestamp settings. (Architecture-related: Platform compatibility) (PRs: #3748, #3952, #3960; commits: d6ee2d5)
- [GT-ZSTD-v1.5.6-0043] Fixed the null pointer dereference problem caused by unchecked memory allocation failure in ZSTD_createCDict_advanced2(). (Architecture-related: public API) (PRs: #3847; commits: 9a3b17c)

### Architecture-related Changes

- [GT-ZSTD-v1.5.6-0062] Upgrade the xxHash library to v0.8.2, including performance optimization and SVE vectorization support, and disabling automatic vectorization of XXH64 by default to avoid performance degradation. (Architecture-related: public API) (PRs: #924, #3819, #3820, #3933; commits: 007cda8, 592b1ac)
- [GT-ZSTD-v1.5.6-0071] Windows build workflow adds win32 architecture support, and changes to a strategy matrix to build win32 and win64 architecture products at the same time. (Architecture-related: platform compatibility) (PRs: #3600; commits: 520843d, a4fff8e)
- [GT-ZSTD-v1.5.6-0073] Fixed the problem of assembly file compilation failure in Intel Xcode build, forcing the source file language to C only when the assembly and C compiler are different. (Architecture-related: platform compatibility) (PRs: #3622, #3665; commits: 7e09f07)
- [GT-ZSTD-v1.5.6-0075] Add a public header file include directory to the library target through the CMake BUILD_INTERFACE generator expression, so that other projects can correctly reference the zstd header file through FetchContent or ExternalProject_Add. (Architecture-related: build and installation methods) (PRs: #3968; commits: 79cd0ff)
- [GT-ZSTD-v1.5.6-0076] Improved CMake configuration to export a unified zstd::libzstd target when only static or dynamic linking is specified. (Architecture-related: build and installation methods) (PRs: #3811; commits: c53d650)
- [GT-ZSTD-v1.5.6-0077] Change zstd::libzstd from an alias target to an imported interface target to dynamically select static or dynamic linking when using find_package. (Architecture-related: build vs. installation mode) (PRs: #3811; commits: 475da4f)
- [GT-ZSTD-v1.5.6-0079] Define and export the zstd::libzstd target uniformly in the CMake project to avoid repeated definitions. (Architecture-related: build and installation methods) (PRs: #3811; commits: dcd713c)
- [GT-ZSTD-v1.5.6-0081] Fix CMake build, when both shared and static libraries are enabled, the libzstd target is always created and its type is determined based on BUILD_SHARED_LIBS. (Architecture-related: build and installation methods) (PRs: #3859, #3965; commits: a0a9bc6)
- [GT-ZSTD-v1.5.6-0082] Fix CMake build: Unify the management of public header files, expose only the include path of the library directory, and set the include directory to INTERFACE. (Architecture-related: public API) (PRs: #3716, #3968; commits: a595e58)
- [GT-ZSTD-v1.5.6-0084] Unify Windows platform detection macros to only check compiler-defined _WIN32 to unify Windows detection methods. (Architecture-related: platform compatibility) (PRs: #3772; commits: 585aaa0)

### Compatibility & Legacy

- [GT-ZSTD-v1.5.6-0065] Modify the bitstream implementation to always return 0 after overflow, and introduce internal overloaded functions to enhance cross-platform behavioral consistency and improve security. (Architecture-related: public API behavior) (PRs: #3676; commits: 74c901b, ba50807)

### Core Compression Engine

- [GT-ZSTD-v1.5.6-0001] api: Promote `ZSTD_c_targetCBlockSize` to Stable API by @felixhandte (PRs: #3915, #3917, #3964, #3977; commits: 038a8a9, 3613448, 68a232c, 6f1215b, f5728da)
- [GT-ZSTD-v1.5.6-0002] api: new `ZSTD_d_maxBlockSize` experimental parameter, to reduce streaming decompression memory, by @terrelln (PRs: #3616, #3617; commits: 0abf2ba, 61efb2a)
- [GT-ZSTD-v1.5.6-0003] perf: improve performance of param `ZSTD_c_targetCBlockSize`, by @Cyan4973 (PRs: #3762, #3826, #3827; commits: 5ab78c0, c7269ad)
- [GT-ZSTD-v1.5.6-0006] lib: improved huffman speed on small data and linux kernel, by @terrelln (PRs: #3762, #3826, #3827; commits: 5ab78c0, c7269ad)
- [GT-ZSTD-v1.5.6-0007] lib: accept dictionaries with partial literal tables, by @terrelln (PRs: #3731, #3737, #3917; commits: 396ef5b, bd02c9b, ef82b21)
- [GT-ZSTD-v1.5.6-0011] lib: fix several bugs in magicless-format decoding, by @embg (PRs: #3830, #3831, #3959, #3976; commits: 741b87b, 8193250, f65b9e2)
- [GT-ZSTD-v1.5.6-0024] build: improve win32 support, by @DimitriPapadopoulos (PRs: #3770; commits: cdceb0f)
- [GT-ZSTD-v1.5.6-0027] port: ARM64EC compatibility for Windows, by @dunhor (PRs: #3636; commits: 1b994cb)
- [GT-ZSTD-v1.5.6-0030] port: risc-v support validation in CI, by @Cyan4973 (PRs: #3731, #3840, #3934; commits: 468bb17, ad59027, bd02c9b)
- [GT-ZSTD-v1.5.6-0031] port: sparc64 support validation in CI, by @Cyan4973 (PRs: #3731, #3840, #3886; commits: 468bb17, bd02c9b, e1ef81a)
- [GT-ZSTD-v1.5.6-0034] doc: Improved specification accuracy, by @elasota (PRs: #3753, #3977; commits: 902c7ec, feaa8ac)
- [GT-ZSTD-v1.5.6-0035] bug: Fix and deprecate ZSTD_generateSequences (#3981) (PRs: #3981; commits: 731f4b7, 86caab5)
- [GT-ZSTD-v1.5.6-0037] The long decoder adapts the new decodeSequences interface, removes the old implementation and optimizes the loop logic to detect corruption earlier. (Architecture-related: core decompression module) (PRs: #3677; commits: c60dced)
- [GT-ZSTD-v1.5.6-0038] Fixed typos and added a new workspace size query function. (Architecture-related: public API) (PRs: #3771; commits: fe34776)
- [GT-ZSTD-v1.5.6-0040] Implement single decompression fallback for magicless format, and add private functions to support magicless frames. (Architecture-related: public API) (PRs: #3971; commits: 7d970bd)
- [GT-ZSTD-v1.5.6-0042] The flexible array mode of Buffer Pool and CCtx Pool in ZSTDMT has been removed and changed to external allocation, which solves the compatibility issue with the new version of ubsan. (Architecture-related: platform compatibility) (PRs: #3786; commits: 6bb1688, c87ad5b, e8ff7d1)
- [GT-ZSTD-v1.5.6-0055] Support compile-time exclusion of individual compression policies, set excluded policy entries in the block compressor table to NULL, and adjust the policy selection logic in CParams to avoid using excluded block compressors, while adding NULL checks and assertions to ensure safety. (Architecture-related: Compile-time policy exclusion) (PRs: #3623; commits: 16bbd74, 1b65803, 59c7b2a, 5a75956, 81b86a2, b7add1d, cbf3e26)
- [GT-ZSTD-v1.5.6-0056] Refactored the ZSTD_sequenceProducer_F type from a function type to a function pointer type, and updated all related uses. (Architecture-related: public API type changes) (PRs: #3839; commits: 809c7eb)
- [GT-ZSTD-v1.5.6-0057] Migrate the parameters of the external sequence generator (ESP) from the compression context to the ZSTD_CCtx_params structure, and add the auxiliary function ZSTD_hasExtSeqProd. (Architecture-related: public API parameter migration) (PRs: #3839; commits: d151a48)
- [GT-ZSTD-v1.5.6-0058] Replaced memcpy with ZSTD_memcpy to support redirection in Linux kernel mode. (Architecture-related: Platform compatibility: Linux kernel mode) (PRs: #3895; commits: fe2e2ad)
- [GT-ZSTD-v1.5.6-0066] Modify the decoding sequence process, add new parameters to detect overflow events, eliminate the need for checksums, and enhance security. (Architecture-related: core decompression behavior) (PRs: #3677; commits: 02134fa)
- [GT-ZSTD-v1.5.6-0067] Stop global suppression of UBSAN pointer overflow, change to local suppression, and introduce auxiliary functions to safely handle pointer operations and fix fuzzer problems. (Architecture-related: public API macro definition) (PRs: #3658, #3738, #3776, #3947; commits: 3daed70, 43118da, b20703f, c27fa39, d01a2c6)
- [GT-ZSTD-v1.5.6-0068] Convert invalid cases at offset 0 to extremely positive numbers so that they are detected as data corruption in distance checks and no longer rely on checksums. (Architecture-related: core decompression behavior) (PRs: #3937; commits: a9fb8d4)
- [GT-ZSTD-v1.5.6-0070] In the format specification, the case where the offset calculation result is 0 is clearly defined as data corruption, and it is added that the decompressor should treat it as offset 1 in this case. At the same time, it is added in the API document of ZSTD_decompressStream: After the operation returns an error, the DCtx state is undefined. Calling this function at this time is undefined behavior, and the state must be reset first. (Architecture-related: public API and format specification) (PRs: #3824, #3977; commits: 5d82c2b, f06b18b)
- [GT-ZSTD-v1.5.6-0072] Added compile-time macro protection, allowing to exclude specific compression strategies during build, and added new build options ZSTD_LIB_EXCLUDE_COMPRESSORS_DFAST_AND_UP and ZSTD_LIB_EXCLUDE_COMPRESSORS_GREEDY_AND_UP to reduce library size. (Architecture-related: Build options) (PRs: #3623; commits: 39b7946, 50cdf84, 5490c75, 6761e1c, b12e8cb, bae1749, cc1ffe0, d09f195, eb92279)
- [GT-ZSTD-v1.5.6-0086] Update the version number to v1.5.6. (Architecture-related: version and compatibility) (PRs: #3969; commits: 686e7e4)

### Cross-cutting / Other Architecture-related Changes

- [GT-ZSTD-v1.5.6-0009] lib: fix corner case decoder behaviors, by @Cyan4973 and @aimuz (PRs: #3753, #3862, #3946; commits: 4edfaa9, e49d1ab, f6039f3)
- [GT-ZSTD-v1.5.6-0017] tests: better compatibility with older versions of `grep`, by @Cyan4973 (PRs: #3807, #3884; commits: 4502ca5, c7611d6, f013b1b)
- [GT-ZSTD-v1.5.6-0019] build: cmake improvements by @terrelln, @sighingnow, @gjasny, @JohanMabille, @Saverio976, @gruenich, @teo-tsirpanis (PRs: #3657, #3957, #3975; commits: 42b02f5, 5059618, c1e9953)
- [GT-ZSTD-v1.5.6-0022] build: fix Apple platform compatibility, by @nidhijaju (PRs: #3688, #3884; commits: b1a30e2, c7611d6)
- [GT-ZSTD-v1.5.6-0026] port: make: fat binaries on macos, by @mredig (PRs: #3614; commits: 0a79416)
- [GT-ZSTD-v1.5.6-0029] port: MSYS2 and Cygwin makefile installation and test support, by @QBos07 (PRs: #3720; commits: 78dbba7)
- [GT-ZSTD-v1.5.6-0033] port: HP-UX compatibility, by @likema (PRs: #3807, #3884, #3913; commits: 4502ca5, 588dfbc, c7611d6, e62e15d, f013b1b)

### Tools & Applications

- [GT-ZSTD-v1.5.6-0013] cli: fix mixing `-c` and `-o` commands with `--rm`, by @Cyan4973 (PRs: #3719, #3850, #3942; commits: 8052cd0, c610a01, fbd9e62)
- [GT-ZSTD-v1.5.6-0020] build: bazel support, by @jondo2010 (PRs: #3739, #3812, #3957; commits: 2538732, 98d8ad2, c1e9953)
- [GT-ZSTD-v1.5.6-0023] build: fix Visual 2012 and lower compatibility, by @Cyan4973 (PRs: #3664, #3929; commits: 2abe8d6, 94a2f27)
- [GT-ZSTD-v1.5.6-0032] port: AIX compatibility, by @likema (PRs: #3860, #3884, #3913; commits: 588dfbc, 66269e7, c7611d6, e62e15d)
- [GT-ZSTD-v1.5.6-0074] The pzstd build configuration removes conditional judgment and directly uses the C++14 standard to solve portability issues. (Architecture-related: build requirements) (PRs: #3682; commits: cd4dba7)
- [GT-ZSTD-v1.5.6-0078] Improved CMake build tests to be compatible with earlier versions of CMake (<3.13), and fixed compilation issues when using CMake to build pzstd on macOS. (Architecture-related: Platform compatibility) (PRs: #3883; commits: 2fc7248)
- [GT-ZSTD-v1.5.6-0080] Stop hardcoding the POSIX version on BSD systems and instead rely on the unistd.h that comes with the system (architecture-related: platform compatibility) (PRs: #3952; commits: f99a450)
- [GT-ZSTD-v1.5.6-0085] Removed the custom type definition for intptr_t because the Linux kernel's <linux/types.h> already provides this type. (Architecture-related: platform compatibility) (PRs: #3822; commits: a419265)

## Routine Changes

### Bug Fixes

- [GT-ZSTD-v1.5.6-0008] lib: fix CCtx size estimation with external sequence producer, by @embg
- [GT-ZSTD-v1.5.6-0014] cli: fix erroneous exclusion of hidden files with `--output-dir-mirror` by @felixhandte (PRs: #3963; commits: 86b8e39)
- [GT-ZSTD-v1.5.6-0021] build: fix cross-compiling for AArch64 with lld by @jcelerier (PRs: #3957; commits: c1e9953)
- [GT-ZSTD-v1.5.6-0044] Fixed the problem of adding null pointers when outputting nothing, avoiding null pointer operations by returning early. (PRs: #3827; commits: dd4de1d)
- [GT-ZSTD-v1.5.6-0045] Optimized the type safety of thread pool memory copy, and fixed the type conversion problem of job count calculation in asynchronous IO reading. (PRs: #3865; commits: e6f4b46)
- [GT-ZSTD-v1.5.6-0046] Fixed a wrong assertion in the compression optimization code. (PRs: #3895; commits: e5af24c)
- [GT-ZSTD-v1.5.6-0047] Fixed assertion errors and unified management of optimal parser table size by introducing ZSTD_OPT_SIZE macro. (PRs: #3895; commits: 5474edb)
- [GT-ZSTD-v1.5.6-0048] Fixed memory sanitizer (msan) warning, initializing uninitialized fields in optimal parser and adjusting conditional judgment. (PRs: #3895; commits: 6c35fb2)
- [GT-ZSTD-v1.5.6-0049] Fix the issue of assertion failure caused by insufficient backward search space, and avoid triggering assertions by adding an extra space. (PRs: #3900; commits: 22574d8)
- [GT-ZSTD-v1.5.6-0050] Fixed an out-of-bounds read issue found in fuzz testing. (PRs: #3902; commits: b0e8580)
- [GT-ZSTD-v1.5.6-0051] Fixed the boundary condition problem of sub-block division when processing incompressible data blocks, and optimized the performance of the target block size parameter. (PRs: #3915; commits: 6b11fc4)
- [GT-ZSTD-v1.5.6-0052] Fixed a pointer arithmetic issue that could occur when processing long sequences longer than 64KB. (PRs: #3915; commits: 3b40100)
- [GT-ZSTD-v1.5.6-0053] Fixed the problem that some sub-blocks were not compressed in the target compression block size mode, and optimized the related processing logic. (PRs: #3915, #3917; commits: 4b51526, aa8592c)
- [GT-ZSTD-v1.5.6-0054] Fixed an issue where the seed queue was underfilled when reading from AsyncIO, ensuring that the loop continues enqueuing until the number of available tasks reaches zero. (PRs: #3940; commits: edab9ee)
- [GT-ZSTD-v1.5.6-0087] fix Visual Studio datagen recipe (commits: 9e711c9)
- [GT-ZSTD-v1.5.6-0088] fix Visual Studio solutions (commits: 3ce4c6e)

### Build and CI

- [GT-ZSTD-v1.5.6-0025] build: better C90 compliance for zlibWrapper, by @emaste
- [GT-ZSTD-v1.5.6-0083] Fix datagen missing lorem related source files in Meson and CMake builds. (PRs: #3890, #3913; commits: b34517a, befcec1, c2d3570, fd03971)
- [GT-ZSTD-v1.5.6-0089] Cirrus-CI: Add FreeBSD 14 (commits: a52d897)
- [GT-ZSTD-v1.5.6-0090] Update FreeBSD CI: drop 12.4 as it is nearly EOL (commits: 20f8df6)
- [GT-ZSTD-v1.5.6-0091] Update FreeBSD CI images to latest supported releases (commits: f307493)

### Functional Changes / Refactorings

- [GT-ZSTD-v1.5.6-0059] Removed old variants in splitLitBuffer decoding path, simplified decoding loop and updated related function signatures. (PRs: #3677; commits: 33fca19, 84e898a)
- [GT-ZSTD-v1.5.6-0060] Refactored the access method of flexible array members in the FSE decompression workspace, changed to obtain the dtable through pointer offset calculation, and added several type conversions and assertions to alleviate UBSan warnings. (PRs: #3785, #3789; commits: d988e00)
- [GT-ZSTD-v1.5.6-0061] Refactor the optimal parser to change the internal storage from sequences to stretches, enabling chaining of predecessor solutions, and adjust memory allocation and conditional compilation accordingly. (PRs: #3895; commits: 4683667)

### New Features

- [GT-ZSTD-v1.5.6-0005] lib: reduce binary size with selective built-time exclusion, by @felixhandte
- [GT-ZSTD-v1.5.6-0012] cli: add common compressed file types to `--exclude-compressed`` by @daniellerozenblit (PRs: #3951; commits: 5a66afa)
- [GT-ZSTD-v1.5.6-0015] cli: improved time accuracy on BSD, by @felixhandte
- [GT-ZSTD-v1.5.6-0016] cli: better errors on argument parsing, by @KapJI (PRs: #3850; commits: 8052cd0)
- [GT-ZSTD-v1.5.6-0041] The internal benchmark supports generating lorem ipsum samples, and allows selecting the sample size via -B#. (PRs: #3913; commits: 7a225c0)

### Performance

- [GT-ZSTD-v1.5.6-0004] perf: improved compression of arrays of integers at high compression, by @Cyan4973 (PRs: #3793, #3895; commits: d31018e, de10f56)
- [GT-ZSTD-v1.5.6-0063] In the btultra2 block compressor, the literal update logic at position pos+1 is optimized to obtain better compression results when litlen==1. (PRs: #3895; commits: 0166b2b)
- [GT-ZSTD-v1.5.6-0064] Optimize the superblock processing performance of the compression engine, including improving the sequence encoding format, optimizing the target compression block size parameter, exiting incompressible data early and improving the sub-block boundary judgment logic. (PRs: #3667, #3668, #3915, #3917; commits: 1f83b7c, 86db607, 8d31e8e, cc45309, f837219)

### Security

- [GT-ZSTD-v1.5.6-0069] Remove unsafe sprintf calls in zstdcli.c, use safe initialization instead, and adjust the error prompt format. (PRs: #3916; commits: 4d2bf7f)

### Tests

- [GT-ZSTD-v1.5.6-0018] tests: lorem ipsum generator as default backup content, by @Cyan4973 (PRs: #3890, #3913; commits: 1e046ce, 1e240af, 3dbd861, 40874d4, 5a1bb4a, 7003c99, 83598aa, d0b7da3)
