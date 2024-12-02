---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-02
---

<span style="color: gray;">Dated: 02-12-2024</span>

# Ch03. case Study Security Hardening - Ms exchange

- CIS Benchmarks case study (MS Exchange Server 2016)
- 2.5 Set 'Do not permanently delete items until the database has been backed up' to 'True' (Scored)
- Profile applicability:
    - Level 1 - Mailbox Services Security
	- Description: This setting allows you to ensure that items are not permanently deleted until the database has been backed up.
	- Rationale: To ensure that accidentally deleted items can be recovered, they should not be permanently deleted until the database is backed up.
	- Audit: Execute the following cmdlet and ensure `RetainDeletedItemsUntilBackup` is set to `True`:

```
Get-MailboxDatabase <Mailbox Database Name> | fl -property RetainDeletedItemsUntilBackup
```

- Remediation: To implement the recommended state, execute the following PowerShell cmdlet:

```
Set-MailboxDatabase <Mailbox Database Name> - RetainDeletedItemsUntilBackup $true
```

- Impact:
    - The impact of enabling this setting should be minimal.
    - More storage space will be required until any pending items are permanently deleted.
- Default value: False
  