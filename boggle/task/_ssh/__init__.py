# Copyright Hybrid Logic Ltd.  See LICENSE file for details.

from ._model import (
    Run, run, run_from_args,
    Sudo, sudo, sudo_from_args,
    Put, put,
    Comment, comment,
    RunRemotely, run_remotely,
    perform_comment, perform_put, perform_sudo
)

__all__ = [
    "Run", "run", "run_from_args",
    "Sudo", "sudo", "sudo_from_args",
    "Put", "put",
    "Comment", "comment",
    "RunRemotely", "run_remotely",
    "perform_comment", "perform_put", "perform_sudo",
]

try:
    # for admin.packaging usage
    from ._keys import (
        ensure_agent_has_ssh_key,
        AgentNotFound, KeyNotFound
    )

    __all__ += [
        "ensure_agent_has_ssh_key",
        "AgentNotFound", "KeyNotFound"
    ]
except ImportError:
    pass
