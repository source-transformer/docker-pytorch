# docker-pytorch

## Instructions

Unfortunately Linux Dev Containers running on Mac's that have access to PyTorch's MPS functionality will be locked out.

To test this - run the following:

```
python3 test_pytorch.py
```

## Alternative to Set Up Environment on Linux Container

setupPython.sh needs to be set as executable otherwise you'll get error:

```
------
 > [dev_container_auto_added_stage_label 3/3] RUN /opt/src/scripts/setupPython.sh:
#0 0.321 /bin/sh: 1: /opt/src/scripts/setupPython.sh: Permission denied
------
ERROR: failed to solve: executor failed running [/bin/sh -c /opt/src/scripts/setupPython.sh]: exit code: 126
[2023-03-05T21:51:23.736Z] Stop (1231 ms): Run: docker buildx build --load --build-arg BUILDKIT_INLINE_CACHE=1 -f /var/folders/xv/y7f17n5d723cs4ybsbg2sl4h0000gn/T/devcontainercli/container-features/0.31.0-1678053082486/Dockerfile-with-features -t vsc-docker-pytorch-5c38d4a8329f6610a2b814798915e8d4 --target dev_containers_target_stage --build-arg VARIANT=bullseye --build-arg _DEV_CONTAINERS_BASE_IMAGE=dev_container_auto_added_stage_label /Users/cassidy/github/docker-pytorch/.devcontainer
[2023-03-05T21:51:23.737Z] Error: Command failed: docker buildx build --load --build-arg BUILDKIT_INLINE_CACHE=1 -f /var/folders/xv/y7f17n5d723cs4ybsbg2sl4h0000gn/T/devcontainercli/container-features/0.31.0-1678053082486/Dockerfile-with-features -t vsc-docker-pytorch-5c38d4a8329f6610a2b814798915e8d4 --target dev_containers_target_stage --build-arg VARIANT=bullseye --build-arg _DEV_CONTAINERS_BASE_IMAGE=dev_container_auto_added_stage_label /Users/cassidy/github/docker-pytorch/.devcontainer
[2023-03-05T21:51:23.737Z]     at hie (/Users/cassidy/.vscode/extensions/ms-vscode-remote.remote-containers-0.282.0/dist/spec-node/devContainersSpecCLI.js:1931:1698)
[2023-03-05T21:51:23.737Z]     at process.processTicksAndRejections (node:internal/process/task_queues:96:5)
[2023-03-05T21:51:23.737Z]     at async FF (/Users/cassidy/.vscode/extensions/ms-vscode-remote.remote-containers-0.282.0/dist/spec-node/devContainersSpecCLI.js:1930:3910)
[2023-03-05T21:51:23.737Z]     at async S7 (/Users/cassidy/.vscode/extensions/ms-vscode-remote.remote-containers-0.282.0/dist/spec-node/devContainersSpecCLI.js:1930:2839)
[2023-03-05T21:51:23.737Z]     at async xie (/Users/cassidy/.vscode/extensions/ms-vscode-remote.remote-containers-0.282.0/dist/spec-node/devContainersSpecCLI.js:1945:2625)
[2023-03-05T21:51:23.737Z]     at async Wf (/Users/cassidy/.vscode/extensions/ms-vscode-remote.remote-containers-0.282.0/dist/spec-node/devContainersSpecCLI.js:1945:3750)
[2023-03-05T21:51:23.737Z]     at async noe (/Users/cassidy/.vscode/extensions/ms-vscode-remote.remote-containers-0.282.0/dist/spec-node/devContainersSpecCLI.js:2069:17325)
[2023-03-05T21:51:23.738Z]     at async roe (/Users/cassidy/.vscode/extensions/ms-vscode-remote.remote-containers-0.282.0/dist/spec-node/devContainersSpecCLI.js:2069:17066)
[2023-03-05T21:51:23.739Z] Stop (1695 ms): Run: /Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Plugin).app/Contents/MacOS/Code Helper (Plugin) --ms-enable-electron-run-as-node /Users/cassidy/.vscode/extensions/ms-vscode-remote.remote-containers-0.282.0/dist/spec-node/devContainersSpecCLI.js up --user-data-folder /Users/cassidy/Library/Application Support/Code/User/globalStorage/ms-vscode-remote.remote-containers/data --container-session-data-folder /tmp/devcontainers-0075a9d2-96a0-429d-b535-fa99bd1652b71678053081199 --workspace-folder /Users/cassidy/github/docker-pytorch --workspace-mount-consistency cached --id-label devcontainer.local_folder=/Users/cassidy/github/docker-pytorch --id-label devcontainer.config_file=/Users/cassidy/github/docker-pytorch/.devcontainer/devcontainer.json --log-level debug --log-format json --config /Users/cassidy/github/docker-pytorch/.devcontainer/devcontainer.json --default-user-env-probe loginInteractiveShell --mount type=volume,source=vscode,target=/vscode,external=true --skip-post-create --update-remote-user-uid-default on --mount-workspace-git-root true
[2023-03-05T21:51:23.739Z] Exit code 1
[2023-03-05T21:51:23.741Z] Command failed: /Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Plugin).app/Contents/MacOS/Code Helper (Plugin) --ms-enable-electron-run-as-node /Users/cassidy/.vscode/extensions/ms-vscode-remote.remote-containers-0.282.0/dist/spec-node/devContainersSpecCLI.js up --user-data-folder /Users/cassidy/Library/Application Support/Code/User/globalStorage/ms-vscode-remote.remote-containers/data --container-session-data-folder /tmp/devcontainers-0075a9d2-96a0-429d-b535-fa99bd1652b71678053081199 --workspace-folder /Users/cassidy/github/docker-pytorch --workspace-mount-consistency cached --id-label devcontainer.local_folder=/Users/cassidy/github/docker-pytorch --id-label devcontainer.config_file=/Users/cassidy/github/docker-pytorch/.devcontainer/devcontainer.json --log-level debug --log-format json --config /Users/cassidy/github/docker-pytorch/.devcontainer/devcontainer.json --default-user-env-probe loginInteractiveShell --mount type=volume,source=vscode,target=/vscode,external=true --skip-post-create --update-remote-user-uid-default on --mount-workspace-git-root true
[2023-03-05T21:51:23.741Z] Exit code 1
```


