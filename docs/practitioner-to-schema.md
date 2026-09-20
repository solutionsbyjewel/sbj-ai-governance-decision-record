# Practitioner-to-Schema Field Mapping

The practitioner artifact is a human-facing representation of the same frozen Decision Record specification.

**Important:** “Applicable Conditional Profiles A–G / None” is noncanonical practitioner completion-aid metadata. It does not map to a profile-membership field in the JSON object.

| Practitioner section | Practitioner label | JSON path | Classification |
|---|---|---|---|
| Record Administration | Decision Record ID | `record_metadata.decision_record_id` | ADMIN |
| Record Administration | Record Status | `record_metadata.record_status` | ADMIN |
| Record Administration | Created At | `record_metadata.created_at` | ADMIN |
| Record Administration | Last Updated | `record_metadata.updated_at` | ADMIN |
| Record Administration | Completion Mode | `record_metadata.generation_mode` | ADMIN |
| LOCATE | Governed Subject / Use Case | `locate.governed_subject` | CORE |
| LOCATE | Governance Decision / Event Type | `locate.decision_event_type` | CORE |
| LOCATE | Governed Scope | `locate.governed_scope` | CORE |
| LOCATE | Execution Instance Identity Reference | `locate.execution_instance_ref` | CONDITIONAL |
| ASSIGN | Accountable Authority | `assign.accountable_authority` | CORE |
| ASSIGN | Authority Source / Principal | `assign.authority_source` | CONDITIONAL |
| ASSIGN | Delegation / Downstream Authority Reference | `assign.delegated_authority_ref` | CONDITIONAL |
| ASSIGN | Evidence-Sufficiency Authority | `assign.evidence_sufficiency_authority` | CONDITIONAL |
| RECORD | Governance Decision / Disposition | `record.decision_disposition` | CORE |
| RECORD | Decision Time | `record.decision_time` | CORE |
| RECORD | Evidence Basis / Evidence References | `record.evidence_refs` | CORE |
| RECORD | Evidence Sufficiency Determination | `record.evidence_sufficiency` | CORE |
| RECORD | Authorization State Change | `record.authorization_state_change` | CONDITIONAL |
| RECORD | Trigger Source | `record.trigger_source` | CONDITIONAL |
| RECORD | Trigger Time | `record.trigger_time` | CONDITIONAL |
| RECORD | Effective Authorization-State-Change Time | `record.authorization_change_effective_time` | CONDITIONAL |
| RECORD | Material Version / Configuration Reference | `record.material_configuration_ref` | CONDITIONAL |
| RECORD | Material Transformation / Handoff Provenance Reference | `record.transformation_provenance_ref` | CONDITIONAL |
| RECORD | Material Environment / External-State Reference | `record.environment_state_ref` | CONDITIONAL |
| RECORD | Applicable Instructions / Governable Context Reference | `record.governable_context_ref` | CONDITIONAL |
| RECORD | Corrective Action Reference | `record.corrective_action_ref` | CONDITIONAL |
| RECORD | Restart / Resumption Decision | `record.restart_resumption_decision` | CONDITIONAL |
| RECORD | Transition Authorization Reference | `record.transition_authorization_ref` | CONDITIONAL |
| RECORD | Consequential Decision / Action Reference | `record.consequential_action_ref` | CONDITIONAL |
| RECORD | Externally Committed Consequence Reference | `record.committed_consequence_ref` | CONDITIONAL |
| RECORD | Retry / Replay / Resumption Relationship | `record.execution_recurrence_ref` | CONDITIONAL |
| RECORD | Parent / Child Execution Relationship | `record.execution_lineage_ref` | CONDITIONAL |
| RECORD | Permissions / Credentials / Tool-Authority Reference | `record.permission_authority_ref` | CONDITIONAL |
| RECORD | Downstream Acceptance / Execution Reference | `record.downstream_execution_ref` | CONDITIONAL |
| SCALE | Scale / Propagation Determination | `scale.scale_determination` | CORE |
| SCALE | Follow-up / Reassessment Condition | `scale.reassessment_condition` | CONDITIONAL |
