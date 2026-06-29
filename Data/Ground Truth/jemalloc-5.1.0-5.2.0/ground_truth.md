# Ground Truth for jemalloc-5.1.0-5.2.0

## Important Changes

### API & Integration Layer

- [GT-JEMALLOC-5.2.0-0003] Log time information for sampled allocations. (@tyleretzel) (PRs: #1267; commits: 5e23f96, b664bd7)
- [GT-JEMALLOC-5.2.0-0005] Output rate for certain counters in malloc_stats. (@zinoale) (PRs: #1388, #1413; commits: 36de518, 8c95713)
- [GT-JEMALLOC-5.2.0-0009] Add mallctl interfaces: (PRs: #1163, #1267; commits: 126e9a8, 226327c, 59e371f, 5ae6e7c, 5e23f96, 6727004, 83e5161, b664bd7, bb071db, c154f58, cb0707c, fe0e399)
- [GT-JEMALLOC-5.2.0-0011] stats.arenas.<i>.extent_avail (@tyleretzel) (PRs: #1163, #1298; commits: 126252a, 226327c, 59e371f, 5ae6e7c, 6727004, 83e5161, bb071db, c154f58, cb0707c, fe0e399)
- [GT-JEMALLOC-5.2.0-0012] stats.arenas.<i>.extents.<j>.n{dirty,muzzy,retained} (@tyleretzel) (PRs: #1298; commits: c14e6c0)
- [GT-JEMALLOC-5.2.0-0013] stats.arenas.<i>.extents.<j>.{dirty,muzzy,retained}_bytes (@tyleretzel) (PRs: #1298; commits: c14e6c0)
- [GT-JEMALLOC-5.2.0-0043] Lower the default number of background threads to 4 (when the feature is enabled). (@interwq) (PRs: #1218, #1374; commits: b293a3e, c4063ce)
- [GT-JEMALLOC-5.2.0-0046] Avoid forced decay on thread termination when using background threads. (@interwq) (PRs: #1218, #1220, #1374; commits: 312352f, b293a3e, c4063ce)
- [GT-JEMALLOC-5.2.0-0047] Disable muzzy decay by default. (@djwatson, @interwq) (PRs: #1421; commits: 8e9a613)
- [GT-JEMALLOC-5.2.0-0049] Fix background thread index issues with max_background_threads. (@djwatson, @interwq) (PRs: #1220; commits: 312352f)
- [GT-JEMALLOC-5.2.0-0064] Added experimental API smallocx, which returns the pointer and actual available size when allocating memory, and changes the symbol name to a version-dependent hash form. (Architecture-related: public API) (PRs: #1270; commits: 01e2a38, 08260a6, 730e57b)
- [GT-JEMALLOC-5.2.0-0067] Added MALLOC_CONF parsing to support dynamic slab size configuration, and added corresponding integration tests. (Architecture-related: configuration items) (PRs: #1104; commits: 5112d9e)
- [GT-JEMALLOC-5.2.0-0068] Refactor the emitter API to make it clearer as a standalone JSON emitter, and add support for outputting raw values in arrays and nested arrays. (Architecture-related: public API) (PRs: #1267; commits: eb261e5)
- [GT-JEMALLOC-5.2.0-0070] Rename experimental_huge_threshold to oversize_threshold, and allow setting to low values (including 0) to disable the feature. (Architecture-related: public API) (PRs: #1411, #1416, #1469; commits: 788a657, 7a815c1, e3db480)
- [GT-JEMALLOC-5.2.0-0073] Add reentrancy protection to the hook function to prevent recursion caused by triggering again during hook execution. (Architecture-related: public API) (PRs: #1163; commits: a7f749c)
- [GT-JEMALLOC-5.2.0-0074] When abort_conf is enabled, it no longer aborts due to unrecognized experimental options, allowing experimental features to be tested normally. (Architecture-related: configuration behavior) (PRs: #1285; commits: 4bc4871)
- [GT-JEMALLOC-5.2.0-0088] Renamed the hooks module to test_hooks, this is a breaking change. (Architecture-related: module rename) (PRs: #1163; commits: c7a87e0)
- [GT-JEMALLOC-5.2.0-0089] Rename the configuration option huge_threshold to experimental_huge_threshold, and mark it as an experimental feature. (Architecture-related: configuration option rename) (PRs: #1235; commits: cdf15b4)
- [GT-JEMALLOC-5.2.0-0090] Remove the experimental smallocx API from the public header file. Users need to add external declarations to use it. (Architecture-related: public API removal) (PRs: #1270; commits: 741fca1)

### Architecture-related Changes

- [GT-JEMALLOC-5.2.0-0093] Added fast paths to free() and sdallocx(), including the new rtree_szind_slab_read_fast function to quickly read szind and slab information from the L1 cache, and removed the frame operation in most calls. (Architecture-related: public API: new rtree_szind_slab_read_fast) (PRs: #1365; commits: 09adf18, 5e79529, 794e29c)
- [GT-JEMALLOC-5.2.0-0097] Restrict suppression of -Wmissing-field-initializer warnings to only compiler versions with the warning bug (GCC < 5.1 and all clang versions). (Architecture-related: Build and Platform Compatibility) (PRs: #1273; commits: fb924dd)

### Cross-cutting / Other Architecture-related Changes

- [GT-JEMALLOC-5.2.0-0007] Add configure options --{enable,disable}-{static,shared} to allow not building unwanted libraries. (@Ericson2314) (PRs: #1394; commits: 4e920d2)
- [GT-JEMALLOC-5.2.0-0008] Add configure option --disable-libdl to enable fully static builds. (@interwq) (PRs: #1244; commits: 1f55a15, 23b15e7)
- [GT-JEMALLOC-5.2.0-0014] Update MSVC builds. (@maksqwe, @rustyx) (PRs: #1417, #1473; commits: 374dc30, f7489dc)
- [GT-JEMALLOC-5.2.0-0018] Link against -pthread instead of -lpthread. (@paravoid) (PRs: #1401, #1402; commits: 4711910)
- [GT-JEMALLOC-5.2.0-0023] Refactor the TSD module. (@davidtgoldblatt) (PRs: #1342; commits: 0ac5243, 9ed3bdc)
- [GT-JEMALLOC-5.2.0-0045] Use arena index for arena-matching checks. (@interwq) (PRs: #1298, #1386; commits: 126252a, 7241bf5)
- [GT-JEMALLOC-5.2.0-0048] Only initialize libgcc unwinder when profiling is enabled. (@paravoid, @interwq) bug fixes (all only relevant to jemalloc 5.x): (PRs: #1441; commits: 18450d0)
- [GT-JEMALLOC-5.2.0-0063] Attempt to build docs by default, however skip doc building when xsltproc is missing. (@interwq, @cmuellner) (PRs: #1430; commits: 9015deb)

### Platform Abstraction Layer

- [GT-JEMALLOC-5.2.0-0001] Implement oversize_threshold, which uses a dedicated arena for allocations crossing the specified threshold to reduce fragmentation. (@interwq) (PRs: #1235, #1412; commits: 1302af4, 350809d, 94a88c2, ff622ee)
- [GT-JEMALLOC-5.2.0-0002] Add extents usage information to stats. (@tyleretzel) (PRs: #1298, #1378, #1396, #1458, #1476; commits: 37b8913, 3f9f283, 441335d, 45bb448, 6fe1163, 711a61f, 98b56ab, c14e6c0, fb56766)
- [GT-JEMALLOC-5.2.0-0004] Support 0 size in sdallocx. (@djwatson) (PRs: #1240, #1298, #1341; commits: 0ff7ff3, 126252a, 4edbb7c)
- [GT-JEMALLOC-5.2.0-0006] Add configure option --enable-readlinkat, which allows the use of readlinkat over readlink. (@davidtgoldblatt) (PRs: #1104, #1244, #1300; commits: 1f55a15, 23b15e7, 5b7fc90, e8ec952)
- [GT-JEMALLOC-5.2.0-0015] Workaround a compiler optimizer bug on s390x. (@rkmisra) (PRs: #1315; commits: 115ce93)
- [GT-JEMALLOC-5.2.0-0016] Make use of pthread_set_name_np(3) on FreeBSD. (@trasz) (PRs: #1354, #1360; commits: ceba1dd, daa0e43)
- [GT-JEMALLOC-5.2.0-0017] Implement malloc_getcpu() to enable percpu_arena for windows. (@santagada) (PRs: #1354, #1360; commits: ceba1dd, daa0e43)
- [GT-JEMALLOC-5.2.0-0019] Make background_thread not dependent on libdl. (@interwq) (PRs: #1244; commits: 2db2d2e)
- [GT-JEMALLOC-5.2.0-0020] Add stringify to fix a linker directive issue on MSVC. (@daverigby) (PRs: #1444, #1445; commits: cbdb180)
- [GT-JEMALLOC-5.2.0-0021] Detect and fall back when 8-bit atomics are unavailable. (@interwq) (PRs: #1449; commits: 06f0850)
- [GT-JEMALLOC-5.2.0-0022] Fall back to the default pthread_create if dlsym(3) fails. (@interwq) (PRs: #1242; commits: 77a71ef)
- [GT-JEMALLOC-5.2.0-0027] Implement opt.oversize_threshold which uses a dedicated arena for requests crossing the threshold, also eagerly purges the oversize extents. Default the threshold to 8 MiB. (@interwq) (PRs: #1412; commits: 350809d)
- [GT-JEMALLOC-5.2.0-0028] Clean compilation with -Wextra. (@gnzlbg, @jasone) (PRs: #1196, #1200, #1452; commits: 14d3686, 3d29d11)
- [GT-JEMALLOC-5.2.0-0029] Refactor the size class module. (@davidtgoldblatt) (PRs: #1104, #1288; commits: 3aba072, 4610ffa, 4f55c0e, e904f81)
- [GT-JEMALLOC-5.2.0-0032] Avoid runtime detection of lazy purging on FreeBSD. (@trasz) (PRs: #1251; commits: 676cdd6)
- [GT-JEMALLOC-5.2.0-0033] Optimize mmap(2) alignment handling on FreeBSD. (@trasz) (PRs: #1251, #1362; commits: 50b473c, f80c97e)
- [GT-JEMALLOC-5.2.0-0035] Rework the malloc() fast path. (@djwatson) (PRs: #1449; commits: b804d0f)
- [GT-JEMALLOC-5.2.0-0036] Rework the free() fast path. (@djwatson) (PRs: #1449; commits: b804d0f)
- [GT-JEMALLOC-5.2.0-0038] Optimize sync / lwsync on PowerPC. (@chmeeedalf) (PRs: #1352; commits: be0749f)
- [GT-JEMALLOC-5.2.0-0042] Deprecate OSSpinLock. (@interwq) (PRs: #1367; commits: 43f3b1a)
- [GT-JEMALLOC-5.2.0-0051] Fix opt.prof_prefix initialization. (@davidtgoldblatt) (PRs: #1104, #1288; commits: 3aba072, 4f55c0e, e904f81)
- [GT-JEMALLOC-5.2.0-0054] Detect whether explicit extent zero out is necessary with huge pages or custom extent hooks, which may change the purge semantics. (@interwq) (PRs: #1302; commits: f459454)
- [GT-JEMALLOC-5.2.0-0059] Add unit tests for the producer-consumer pattern. (@interwq) (PRs: #1378, #1396, #1476; commits: 37b8913, 3f9f283, 441335d, 45bb448, 6fe1163, 711a61f, 98b56ab)
- [GT-JEMALLOC-5.2.0-0060] Add Cirrus-CI config for FreeBSD builds. (@jasone) (PRs: #1301; commits: 0771ff2)
- [GT-JEMALLOC-5.2.0-0065] A new global slow path mechanism is added, allowing any thread to force other threads to enter the slow path the next time they obtain TSD; at the same time, the TSD state access method is restructured, using atomic operations and encapsulated functions instead. (Architecture-related: internal mechanism) (PRs: #1163; commits: 0379235, e870829)
- [GT-JEMALLOC-5.2.0-0066] A new Seq module is added, which implements a simple seqlock to provide fast read and write concurrency support when there are few write operations. (Architecture-related: concurrency primitives) (PRs: #1163; commits: 06a8c40)
- [GT-JEMALLOC-5.2.0-0069] Add TSD support for multi-threaded fork scenarios and ensure that the tsd_nominal_tsds list in the child process is in a reasonable state. (Architecture-related: fork compatibility) (PRs: #1293; commits: 41b7372)
- [GT-JEMALLOC-5.2.0-0076] Fix the bug of tcache_flush, and add detection of invalid tcache id. When encountering an invalid id, the program will be terminated directly. (Architecture-related: public API) (PRs: #1369; commits: 1f56115)
- [GT-JEMALLOC-5.2.0-0077] Avoid creating unnecessary background threads for huge arenas that default to eager purging, while retaining the ability to create background threads when the user explicitly sets a non-zero decay time. (Architecture-related: public API) (PRs: #1409; commits: bbe8e6a)
- [GT-JEMALLOC-5.2.0-0078] Avoid duplicate definition of tsd_t type, fix build failure when integrating with FreeBSD libc. (Architecture-related: platform compatibility) (PRs: #1442; commits: dca7060)
- [GT-JEMALLOC-5.2.0-0086] Change the state access of thread local storage (TSD) to a functional interface, and change the state field to an atomic type to prepare for subsequent remote modification of the thread state. (Architecture-related: TSD state interface) (PRs: #1163; commits: 39d6420, 982c10d)
- [GT-JEMALLOC-5.2.0-0087] Change the inline mode of atomic operations from static inline to forced inline. (Architecture-related: public API inline mode) (PRs: #1163; commits: e74a1a3)
- [GT-JEMALLOC-5.2.0-0092] Optimized the implementation of pow2_ceil_u64 and pow2_ceil_u32 using built-ins or assembly instructions on supported platforms, and excluded the s390 architecture. (Architecture-related: Platform Compatibility: Exclude s390) (PRs: #1303; commits: 4c548a6)

### Profiling & Statistics Layer

- [GT-JEMALLOC-5.2.0-0075] Fixed the sampling counting memory regression caused by reconstruction, and added a fast path check function to ensure that sampling counting is performed correctly when tdata is empty. (Architecture-related: public API) (PRs: #1351; commits: 936bc2a)
- [GT-JEMALLOC-5.2.0-0098] Changed the type of bytes_until_sample from uint64_t to int64_t to optimize assembly generation on x86 architecture, and adjusted the sampling accumulation logic. (Architecture-related: public API) (PRs: #1342; commits: 997d86a)

## Routine Changes

### Bug Fixes

- [GT-JEMALLOC-5.2.0-0079] Fixed the assertion error in the page cleanup function. When the configured page size is larger than the system page size, the assertion will no longer be triggered by mistake. Instead, it will check whether the address is aligned with the system page size. (PRs: #1217; commits: e8a63b8)
- [GT-JEMALLOC-5.2.0-0080] Fixed a regression in tcache_bin_flush_large where the wrong arena variable was used, resulting in incorrect lock operations. (PRs: #1258; commits: fec1ef7)
- [GT-JEMALLOC-5.2.0-0081] Adjust the calling timing of prof_boot0 to avoid opt_prof_prefix being overwritten during the boot process. (PRs: #1325; commits: 88771fa)
- [GT-JEMALLOC-5.2.0-0082] Fix the problem of incorrectly calling tcache_destroy in the tcaches_flush function and use tcache_flush_cache instead for correct cache flushing. (PRs: #1368; commits: cd2931a)
- [GT-JEMALLOC-5.2.0-0083] Fixed an error in statistics merging in sharded bins, and adjusted the merging logic to avoid repeated counting when all items in the same arena are not refreshed. (PRs: #1389; commits: 99f4eef)
- [GT-JEMALLOC-5.2.0-0084] Fix compilation warning: In configuration processing, change the check parameter of opt_lg_extent_max_active_fit from yes to no to avoid performing minimum value check on it. (PRs: #1472; commits: 0101d5e)
- [GT-JEMALLOC-5.2.0-0085] In prof_log related functions, changed internal memory allocation from ialloc to iallocztm to avoid potential lock order reversal issues. (PRs: #1476; commits: 978a7a2)
- [GT-JEMALLOC-5.2.0-0104] Fix MSVC build (commits: ce5c073)

### Build and CI

- [GT-JEMALLOC-5.2.0-0058] Update the test scripts for FreeBSD. (@devnexen) (PRs: #1258, #1341, #1473; commits: 2b112ea, 5082001, f7489dc)
- [GT-JEMALLOC-5.2.0-0099] Revert "Customize cloning to include tags so that VERSION is valid." (commits: b6f1f26)
- [GT-JEMALLOC-5.2.0-0100] Revert "Remove --branch=${CIRRUS_BASE_BRANCH} in git clone command." (commits: 225d899)
- [GT-JEMALLOC-5.2.0-0101] Remove --branch=${CIRRUS_BASE_BRANCH} in git clone command. (commits: fc13a7f)
- [GT-JEMALLOC-5.2.0-0102] Customize cloning to include tags so that VERSION is valid. (commits: 646af59)
- [GT-JEMALLOC-5.2.0-0103] Add Cirrus-CI config for FreeBSD builds (commits: 6910fcb)

### Functional Changes / Refactorings

- [GT-JEMALLOC-5.2.0-0062] Remove --with-lg-page-sizes. (@davidtgoldblatt) (PRs: #1104; commits: 5b7fc90)
- [GT-JEMALLOC-5.2.0-0091] Move the link fields in the TSD linked list inside the tcache structure to optimize cache utilization. (PRs: #1261; commits: d1e11d4)

### New Features

- [GT-JEMALLOC-5.2.0-0010] opt.oversize_threshold (@interwq) (PRs: #1471; commits: ce03e4c)
- [GT-JEMALLOC-5.2.0-0071] Added lg_ceil function, added corresponding unit tests, and re-added bit_util test to Makefile. (PRs: #1104; commits: 2f07e92)
- [GT-JEMALLOC-5.2.0-0072] Added page customization function and added corresponding unit tests. (PRs: #1104; commits: a7f68ae)

### Performance

- [GT-JEMALLOC-5.2.0-0024] Avoid taking extents_muzzy mutex when muzzy is disabled. (@interwq) (PRs: #1226; commits: d22e150)
- [GT-JEMALLOC-5.2.0-0025] Avoid taking large_mtx for auto arenas on the tcache flush path. (@interwq) (PRs: #1228; commits: c834912)
- [GT-JEMALLOC-5.2.0-0026] Optimize ixalloc by avoiding a size lookup. (@interwq) (PRs: #1240; commits: 0ff7ff3)
- [GT-JEMALLOC-5.2.0-0030] Refactor the stats emitter. (@tyleretzel) (PRs: #1239, #1298, #1413; commits: 126252a, 8c95713, 9bd8deb)
- [GT-JEMALLOC-5.2.0-0031] Optimize pow2_ceil. (@rkmisra) (PRs: #1240, #1342, #1356; commits: 0ff7ff3, d1a861f, d66f976)
- [GT-JEMALLOC-5.2.0-0034] Improve error handling for THP state initialization. (@jsteemann)
- [GT-JEMALLOC-5.2.0-0037] Refactor and optimize the tcache fill / flush paths. (@djwatson) (PRs: #1427, #1469; commits: a4d017f, e13400c)
- [GT-JEMALLOC-5.2.0-0039] Bypass extent_dalloc() when retain is enabled. (@interwq) (PRs: #1361; commits: 8dabf81)
- [GT-JEMALLOC-5.2.0-0040] Optimize the locking on large deallocation. (@interwq) (PRs: #1356; commits: d66f976)
- [GT-JEMALLOC-5.2.0-0041] Reduce the number of pages committed from sanity checking in debug build. (@trasz, @interwq) (PRs: #1371; commits: 57553c3)
- [GT-JEMALLOC-5.2.0-0044] Optimize the trylock spin wait. (@djwatson) (PRs: #1382; commits: b23336a)
- [GT-JEMALLOC-5.2.0-0050] Fix stats output for opt.lg_extent_max_active_fit. (@interwq) (PRs: #1239; commits: 9bd8deb)
- [GT-JEMALLOC-5.2.0-0052] Properly trigger decay on tcache destroy. (@interwq, @amosbird) (PRs: #1366; commits: 7ee0b6c)
- [GT-JEMALLOC-5.2.0-0053] Fix tcache.flush. (@interwq)
- [GT-JEMALLOC-5.2.0-0055] Fix a side effect caused by extent_max_active_fit combined with decay-based purging, where freed extents can accumulate and not be reused for an extended period of time. (@interwq, @mpghf)
- [GT-JEMALLOC-5.2.0-0056] Fix a missing unlock on extent register error handling. (@zoulasc) (PRs: #1472; commits: 59d9891)
- [GT-JEMALLOC-5.2.0-0094] Changed critical size classes (max_small_class, min_large_class, max_large_class) to static constants to avoid accessing extra cache lines in the fast path. (PRs: #1104; commits: 55e5cc1)
- [GT-JEMALLOC-5.2.0-0095] Added a fast path for malloc, assuming the size is within the search range and hits tcache, otherwise it falls back to the default path; malloc is treated as a leaf function through tail call optimization, reducing the caller's overhead of saving registers. (PRs: #1340, #1345; commits: 0f83136, 325e330)

### Security

- [GT-JEMALLOC-5.2.0-0096] Add a check on the return value of malloc_read_fd in pages.c to avoid security issues caused by out-of-bounds memory access after negative values are converted to unsigned types. (PRs: #1337; commits: 856319d)

### Tests

- [GT-JEMALLOC-5.2.0-0057] Simplify the Travis script output. (@gnzlbg) (PRs: #1272; commits: 0eb0641)
- [GT-JEMALLOC-5.2.0-0061] Add size-matching sanity checks on tcache flush. (@davidtgoldblatt, @interwq) (PRs: #1427, #1469; commits: a4d017f, e13400c)
