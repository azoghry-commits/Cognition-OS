# OpenClaw adapter

The package includes `openclaw.plugin.json` with the shared `skills` root.

```powershell
openclaw plugins install --link .
openclaw plugins inspect cognition-os --runtime --json
```

For an immutable local artifact, extract `dist/cognition-os-0.5.0.zip` and install that directory instead of linking the checkout. Restart or refresh the Gateway/session after installation. Use `openclaw skills verify` for trust metadata and run a semantic analysis task for behavior acceptance.

The plugin does not request tools or configuration secrets. Its Python helper remains optional and subject to the host's shell permissions.
