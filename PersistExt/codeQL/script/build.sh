#!/usr/bin/bash
bazel clean --expunge
bazel build --spawn_strategy=local --nouse_action_cache --noremote_accept_cached --noremote_upload_local_results --local_ram_resources=HOST_RAM*.5 --local_cpu_resources=HOST_CPUS*.5 //tensorflow/tools/pip_package:build_pip_package
bazel shutdown
