# Ground Truth for jemalloc-5.2.0-5.2.1

## Important Changes

### Architecture-related Changes

- [GT-JEMALLOC-5.2.1-0025] Added --enable-documentation build option, allowing users to disable document building, and the installation target will conditionally include document installation based on this option. (Architecture-related: build and installation methods) (PRs: #1488; commits: 702d76d)

### Cross-cutting / Other Architecture-related Changes

- [GT-JEMALLOC-5.2.1-0007] Fix the TLS_MODEL attribute in headers. This regression was first released in 5.0.0. (@zoulasc, @interwq) (PRs: #1460, #1482; commits: 1aabab5)
- [GT-JEMALLOC-5.2.1-0008] Implement opt.retain on Windows and enable by default on 64-bit. (@interwq, @davidtgoldblatt) (PRs: #1545, #1567; commits: 9f6a9f4, badf8d9)

### Debugging & Profiling Layer

- [GT-JEMALLOC-5.2.1-0003] Fix the prof_log unit test which may observe unexpected backtraces from compiler optimizations. The test was first added in 5.2.0. (@marxin, @gnzlbg, @interwq) (PRs: #1478, #1520, #1521, #1576; commits: 82b8aaa, c2a3a7c, d26636d, e0a0c8d)
- [GT-JEMALLOC-5.2.1-0005] Fix an incorrect reference in jeprof. This functionality was first released in 3.0.0. (@prehistoric-penguin) (PRs: #1478, #1520, #1521, #1576; commits: 82b8aaa, c2a3a7c, d26636d, e0a0c8d)
- [GT-JEMALLOC-5.2.1-0010] Add format annotation to the format generator function. (@zoulasc) (PRs: #1460, #1556; commits: 020b5dc, 7618b0b, 7f7935c)
- [GT-JEMALLOC-5.2.1-0014] Made architectural adjustments to the profiling module: first tried to split the core data management and logging functions into independent modules, then rolled back these splits, restored the original module structure, and adjusted the visibility of related functions and variables. (Architecture-related: public API and module responsibilities) (PRs: #1556, #1574; commits: 0b46240, 1a05033, 5742473)
- [GT-JEMALLOC-5.2.1-0016] Added a new red zone check function for small sample allocation, and supports custom abort processing through the configurable abort function. (Architecture-related: public API: redzone check and abort configuration) (PRs: #1465, #1539; commits: 21cfe59, 33e1dad, 7720b6e, b92c9a1)
- [GT-JEMALLOC-5.2.1-0018] Added nonfull_slabs counter to bin statistics and displayed in statistical output. (Architecture-related: public API: nonfull_slabs statistics) (PRs: #1486; commits: 7fc4f2a)
- [GT-JEMALLOC-5.2.1-0019] Added confirm_conf option. When enabled, all configuration strings and the setting process of each option will be printed at startup. (Architecture-related: public API: confirm_conf) (PRs: #1498, #1568; commits: 85f0cb2, c92ac30)
- [GT-JEMALLOC-5.2.1-0020] Add nfills and nflushes tracking and output for arena's small and large allocation statistics. (Architecture-related: public API: nfills/nflushes statistics) (PRs: #1501; commits: 07c4484)
- [GT-JEMALLOC-5.2.1-0023] Added abandoned_vm counter, used to track virtual memory space leaked due to metadata allocation failure (OOM), and expose this indicator in statistical output. (Architecture-related: public API) (PRs: #1553; commits: 4e36ce3)
- [GT-JEMALLOC-5.2.1-0024] Fix the memory leak caused by not supporting split when retain is disabled on the Windows platform, and adjust the allocation strategy to only perform exact matching to avoid split and merge operations. (Architecture-related: platform compatibility) (PRs: #1545, #1573; commits: 57dbab5, c9cdc1b)

### Platform Abstraction Layer

- [GT-JEMALLOC-5.2.1-0022] Implement the retain function on Windows, by tracking the header extent status of each VirtualAlloc area, and restrict the merge and split operations to only be performed in the same area to correctly support MEM_DECOMMIT. (Architecture-related: platform compatibility) (PRs: #1545; commits: 9a86c65)

### User API Layer

- [GT-JEMALLOC-5.2.1-0002] Fix size 0 handling in posix_memalign(). This regression was first released in 5.2.0. (@interwq) (PRs: #1554, #1562; commits: 1d148f3, b62d126, f32f23d)
- [GT-JEMALLOC-5.2.1-0009] Optimize away a branch on the operator delete[] path. (@mgrice) (PRs: #1451; commits: d3d7a8e)
- [GT-JEMALLOC-5.2.1-0015] Added experimental.utilization namespace to provide memory utilization analysis function, support input of single pointer or pointer array and output memory utilization statistics. (Architecture-related: public API: experimental.utilization) (PRs: #1463, #1480, #1505; commits: 4c63b0e, 7ee3897, 9aab3f2)
- [GT-JEMALLOC-5.2.1-0017] Expose the opt_safety_checks configuration item through the mallctl interface, and output the configuration value in statistical information. (Architecture-related: public API: opt_safety_checks) (PRs: #1465; commits: f95a88f)
- [GT-JEMALLOC-5.2.1-0021] Added experimental mallctl experimental.arenas.i.pactivep, which is used to quickly read the pactive counter of arena and avoid going through the mallctl/epoch step. (Architecture-related: public API: experimental.arenas.i.pactivep) (PRs: #1508; commits: e13cf65)

## Routine Changes

### Bug Fixes

- [GT-JEMALLOC-5.2.1-0001] Fix a severe virtual memory leak on Windows. This regression was first released in 5.0.0. (@Ignition, @j0t, @frederik-h, @davidtgoldblatt, @interwq)
- [GT-JEMALLOC-5.2.1-0006] Fix an assertion on the deallocation fast-path. This regression was first released in 5.2.0. (@yinan1048576)

### Build and CI

- [GT-JEMALLOC-5.2.1-0026] Add missing safety_check.c to MSBuild projects (commits: 40a3435)

### Performance

- [GT-JEMALLOC-5.2.1-0004] Fix the declaration of the extent_avail tree. This regression was first released in 5.1.0. (@zoulasc)
- [GT-JEMALLOC-5.2.1-0011] Refactor and improve the size class header generation. (@yinan1048576) (PRs: #1487; commits: ae124b8)
- [GT-JEMALLOC-5.2.1-0012] Remove best fit. (@djwatson) (commits: 5679751)
- [GT-JEMALLOC-5.2.1-0013] Avoid blocking on background thread locks for stats. (@oranagra, @interwq) (PRs: #1510; commits: 1a71533)
