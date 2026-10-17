# Capability Scan

Copy this file to `agents/local/CAPABILITIES.md` and fill it in. It is **local and
never committed** — it describes your machine and your agent, not the project.
See `agents/LOCAL_SETUP.md`.

Date of this scan: fill in. Re-scan when the environment changes.

## Platform

Name the agent, the model, and where it is running.

## Agent Capabilities

Record what was verified, not what was assumed.

| Capability | Available | Evidence / Notes |
|---|---|---|
| File read/write | unknown | Not checked |
| Shell commands | unknown | Not checked |
| Subagents | unknown | Not checked |
| Parallel tool calls | unknown | Not checked |
| Browser/UI inspection | unknown | Not checked |
| Network access | unknown | Not checked |
| GitHub/PR tooling | unknown | Not checked |
| Sandboxes or git worktrees permitted | unknown | Not checked |
| Image/PDF/doc generation | unknown | Not checked |

## Displays

Detect how many monitors this machine has, and record their layout from the
command output rather than from assumption. Use the command for your platform:

- Windows (PowerShell): `Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Screen]::AllScreens`
- macOS: `system_profiler SPDisplaysDataType`
- Linux: `xrandr --listmonitors`

| Fact | Value |
|---|---|
| Monitor count | fill in |
| Layout (name, resolution, position, primary) | fill in |
| Agent-spawned windows open on | fill in |

If there is more than one monitor, ask the owner: "If an agent has to spawn a
window (an app under test, a viewer, a browser), on which monitor should it
open?" Record the answer in the table above. Agents honour it whenever they
launch anything with a window: they pass launch options that target that
screen, or move the window there after launch. If the owner has no preference,
record that. With one monitor, record the count and skip the question.

## Connected Integrations

List integrations and which are actually authorised. One that is configured but
unauthorised is not a capability, and planning around it will fail at the moment
it is needed.

## Machine Facts

Paths and binaries that exist only here. Anything recorded in this section must
not appear in the committed harness.

| Fact | Value |
|---|---|
| Checkout location | fill in |
| Other working trees | fill in |
| Project binaries and versions | fill in |

## Isolation Strategy

How you keep concurrent work from sharing a working tree — separate clones, git
worktrees, containers, or working serially. The committed workflow states only
the principle; the mechanism is yours and belongs here.

## Subagent Policy

- If subagents are available, use them for plan review, implementation review,
  adversarial verification, research, and parallel read-only inspection.
- If subagents are not available, document the downgrade and perform a labeled
  single-agent review.
- Never pretend a simulated role is an autonomous subagent.

## Downgrades

List capability downgrades and their effect on harness strength.
