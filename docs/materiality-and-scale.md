# Materiality and Machine Scale

A Decision Record is created for a **material governance decision or material governance event requiring an attributable determination**.

It is not created merely because an AI system produced another model call, tool call, agent step, branch, retry, sensor event, actuator command, conversation, process, or telemetry event.

Those execution records can remain in specialized systems and be referenced when material.

## Scale

`scale.scale_determination` identifies how broadly a governance determination applies. A decision affecting one execution should not automatically govern an entire system. Propagation should remain within the scope supported by authority and evidence.

## Machine-generated support

The record supports `HUMAN`, `MACHINE`, and `HYBRID` generation. Many machine-generated execution/evidence records can support one material governance Decision Record. This keeps governance reconstructable without converting the Decision Record into a machine-event database.
