---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-12
---

<span style="color: gray;">Dated: 12-11-2024</span>

# Ch02. Backup Strategies

## Backup Considerations

- What to backup?
- Backup location?
- Freq of backup?
- Backup operator?
- Backup checker (verification)?
- Backup test & security methods?
- Technology & tools used for backup?

## What to Backup

- Network configuration files
- OS backups
- Database and application data
- Other critical data

## Backup Location

- Onsite for faster recovery
- Offsite for DR purposes
- Intermediate site (secondary site) as middle ground

## Backup Frequency

- Depends entirely on criticality of data, nature of the information being backed up (how frequently does info change?), storage space available, and overall backup plan

## Backup Operator and Checker

- Backups should ideally be automated
- Operator should ensure that backups have taken place
- Verifier should sign-off that check has been made

## Backup Testing and Security Considerations

- Backup testing should be performed on a periodic basis and greater than frequency of the DR drill (e.g. DR drill once a QTR and testing once a month)
- Encryption and compression

## Backup Tools and Technology

- Consider NAS, SAN, SCSI/IDE/SATA drives
- Various tools and technology to perform full, differential, and incremental backups
- Encryption
- Access control
- Alerts & reporting