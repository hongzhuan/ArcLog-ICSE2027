# Ground Truth for zstd-v1.5.4-v1.5.5

## Important Changes

### API Abstraction Layer (Layer 1)

- [GT-ZSTD-v1.5.5-0003] lib: deprecated bufferless block-level API (#3534) by @terrelln (PRs: #3534; commits: fbd97f3)
- [GT-ZSTD-v1.5.5-0008] cli: fix decompression into block device using -o, reported by @georgmu (#3583) (PRs: #3583, #3584, #3589; commits: 130c264, 14d0cd5, 2e29728, 5bf1359)
- [GT-ZSTD-v1.5.5-0018] Added ZSTD_setFParams() and ZSTD_setParams() auxiliary functions, unified parameter setting interface, and supplemented unit testing and documentation. (Architecture-related: public API) (PRs: #3396, #3530; commits: 07a2a33)
- [GT-ZSTD-v1.5.5-0028] Clarify the requirements of dstCapacity in the single compression function to ensure that compression will succeed when sufficient space is provided. (Architecture-related: public API) (PRs: #3524, #3531; commits: c40c737)
- [GT-ZSTD-v1.5.5-0029] Supplementary documentation for ZSTD_CCtx_loadDictionary and ZSTD_CCtx_refPrefix to explain the compatibility differences between LDM (long distance mode) and dictionaries. (Architecture-related: public API) (PRs: #3553; commits: f4563d8)
- [GT-ZSTD-v1.5.5-0036] The version number has been updated to v1.5.5, and the manual page has been updated simultaneously. (Architecture-related: version and compatibility) (PRs: #3577; commits: 9f58241)

### Application and Integration Layer (Layer 3)

- [GT-ZSTD-v1.5.5-0004] cli: mmap large dictionaries to save memory, by @daniellerozenblit (PRs: #3486, #3557; commits: 2d8afd9, 4373c5a, 610c8b9, 96e55c1, b2ad17a)
- [GT-ZSTD-v1.5.5-0006] cli: improve i/o speed (~+10%) when processing lots of small files (#3479) by @felixhandte (PRs: #3479; commits: 1c42844, a5a2418, f746c37)
- [GT-ZSTD-v1.5.5-0009] build: fix zstd CLI compiled with lzma support but not zlib support (#3494) by @Hello71 (PRs: #3022, #3490, #3494, #3497; commits: 183a18a, 886de7b, 97ab0e2)
- [GT-ZSTD-v1.5.5-0024] Simplify the benchmark API, change the return type of BMK_syntheticTest, BMK_benchFilesAdvanced and BMK_benchFiles from BMK_benchOutcome_t to int, directly return integer error code. (Architecture event: HighResTimer module change) (PRs: #3526; commits: 1e38e07, db79219)
- [GT-ZSTD-v1.5.5-0033] In the build configuration of contrib/pzstd, added logic to automatically detect and select the latest C++ standard (minimum C++11) supported by the compiler. (Architecture-related: Build requirements: C++11 minimum standard) (PRs: #3499, #3574; commits: 1b8bddc)
- [GT-ZSTD-v1.5.5-0034] Modify the build configuration of pzstd and explicitly set -std=c++11 only when the default C++ standard is lower than C++11, otherwise the compiler default standard is used. (Architecture-related: Build requirements: C++11 conditional setting) (PRs: #3574; commits: cbe0f0e)

### Architecture-related Changes

- [GT-ZSTD-v1.5.5-0019] Initialize the compression level field in the static CDict, fix the problem of user-defined MOREFLAGS and FUZZER_FLAGS being overwritten in the Makefile, and add the MSAN fuzz non-optimized CI workflow. (Architecture-related: build and installation methods) (PRs: #3525, #3527; commits: 988ce61)
- [GT-ZSTD-v1.5.5-0020] Correct the assert macro definition, change WARN_ON((x)) to WARN_ON(!(x)), so that it can trigger the assertion correctly. (Architecture-related: platform compatibility) (PRs: #3532; commits: 6313a58)
- [GT-ZSTD-v1.5.5-0030] Added GitHub Actions workflow for generating release artifacts in Windows 64-bit environment. (Architecture-related: Build and Release: Windows 64-bit artifacts) (PRs: #3491; commits: f37b291)
- [GT-ZSTD-v1.5.5-0031] Fixed third-party action dependencies in the GitHub Actions workflow from version tags to specific commit hashes to improve supply chain security. (Architecture-related: Build Security: Fixed Third-Party Action Dependencies) (PRs: #3542; commits: 1ec5562)
- [GT-ZSTD-v1.5.5-0032] Fixed the dependency hash of the base image in the Dockerfile. (Architecture-related: Build repeatability: Fixed base image dependencies) (PRs: #3542; commits: cd94860)
- [GT-ZSTD-v1.5.5-0035] Adjust the naming and directory structure of Windows release artifacts to be consistent with the v1.5.0 version specification, and update the CI workflow to automatically execute when an event is released. (Architecture-related: Release Artifact Structure) (PRs: #3591; commits: fcaa422)

### Core Compression Engine (Layer 0)

- [GT-ZSTD-v1.5.5-0021] Fixed an overread issue that could occur when decompressing certain invalid magic-less frames or requesting invalid skippable frame attributes. (Architecture-related: decompression behavior) (PRs: #3592; commits: e4120c5)

### Cross-cutting / Other Architecture-related Changes

- [GT-ZSTD-v1.5.5-0002] perf: improve mid-level compression speed (#3529, #3533, #3543, @yoniko and #3552, @terrelln) (PRs: #3528, #3529, #3533, #3543, #3548, #3552; commits: 33e3909, 91f4c23, 9420bce, a3c3a38, a91e91d)
- [GT-ZSTD-v1.5.5-0010] build: fix cmake does no longer require 3.18 as minimum version (#3510) by @kou (PRs: #3392, #3500, #3510; commits: 8420502)
- [GT-ZSTD-v1.5.5-0011] build: fix MSVC+ClangCL linking issue (#3569) by @tru (PRs: #3522, #3569, #3579; commits: 0f77956, 871f3a4, 979b047)
- [GT-ZSTD-v1.5.5-0012] build: fix zstd-dll, version of zstd CLI that links to the dynamic library (#3496) by @yoniko (PRs: #3496; commits: c78f434)
- [GT-ZSTD-v1.5.5-0014] doc: updated zstd specification to clarify corner cases, by @Cyan4973 (PRs: #3508, #3514, #3538, #3544; commits: 1df9f36, 64e8511, 832f559)
- [GT-ZSTD-v1.5.5-0015] doc: document how to create fat binaries for macos (#3568) by @rickmark (PRs: #3568; commits: 408bd1e, 82cf603, abb3585, c36d54f)
- [GT-ZSTD-v1.5.5-0016] misc: improve seekable format ingestion speed (~+100%) for very small chunk sizes (#3544) by @Cyan4973 (PRs: #3544; commits: 134d332, 1df9f36)

## Routine Changes

### Bug Fixes

- [GT-ZSTD-v1.5.5-0001] fix: fix rare corruption bug affecting the high compression mode, reported by @danlark1 (#3517, @terrelln) (PRs: #3517; commits: 395a2c5)
- [GT-ZSTD-v1.5.5-0007] cli: zstd no longer crashes when requested to write into write-protected directory (#3541) by @felixhandte (PRs: #3541; commits: 283c228, c4c3e11)
- [GT-ZSTD-v1.5.5-0013] build: fix MSVC warnings (#3495) by @embg (PRs: #3495; commits: a7de1d9)
- [GT-ZSTD-v1.5.5-0022] Fixed an issue where the window size did not take into account the full dictionary contents when loading a dictionary, and adjusted the dictionary truncation threshold to support larger index tables. (PRs: #3556; commits: 3e0550e)
- [GT-ZSTD-v1.5.5-0023] Added a check for destination buffer validity when decompressing, and added a fuzz test to randomize the destination pointer when zero-sized buffers are used. (PRs: #3555; commits: fcaf06d)

### Performance

- [GT-ZSTD-v1.5.5-0005] cli: improve speed of --patch-from mode (~+50%) (#3545) by @daniellerozenblit (PRs: #3545; commits: 53bad10)
- [GT-ZSTD-v1.5.5-0025] Optimized the performance of forward jump when decompressing the seekable format to avoid repeatedly reading frame data when jumping multiple small intervals within the same frame. (PRs: #3581; commits: 618bf84)
- [GT-ZSTD-v1.5.5-0026] Mark the BIT_reloadDStream function as forced inline to improve the decompression speed under PGO optimized compilation. (PRs: #3576; commits: e6dccbf)
- [GT-ZSTD-v1.5.5-0027] Removed Clang-only branch prediction hints in ZSTD_decodeSequence to improve decompression performance when PGO is enabled. (PRs: #3576; commits: b558190)

### Tests

- [GT-ZSTD-v1.5.5-0017] misc: tests/fullbench can benchmark multiple files (#3516) by @dloidolt (PRs: #3516; commits: 4b9e3d1, db7d7b6)
