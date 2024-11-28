# Winget

Windows package manager.  
It also uses a `YAML` file to configure the whole PC according to what you want.

## Sections

### Assertions

Preconditions required to run the configuration.  
They run in parallel to check if your machine matches the pre-requirements.  

#### Failure

If any assertion returns `false`, then any resource using `dependsOn` field relative to that assertion, will fail to run.

### Resources

- Tools to install
- Configurations for
	- Tools installed
	- Windows

## How to Write

The configuration file should be named `configuration.dsc.yaml` and for github based projects, it should be inside `configurations` parent directory.

### Schema

The first line should contain the following `comment`.

```yaml
# yaml-language-server: $schema=https://aka.ms/configuration-dsc-schema/0.2
```

where the `0.2` is version number which updates over time.

### Root

The root `node` is `properties` and it should have a `configurationVersion` key to keep track of how the configuration changes over time.  
It is advisable to use `semantic versioning`[^1] for this.  
The root `node` should also contain `assertions` and `resources` `nodes`.

### Resource

This `node` must contain `directives` and `settings` key.  
Optionally, an `id` key to give it a unique identifier.  
Resource name should be in format of `{ModuleName}/{DscResource}`  
Where `ModuleName` is the `PowerShell` module and `DscResource` is the name of the `DSC resource`[^2] of that module.

#### Directives

This should contain a `description` key to describe the task.  
The `allowPrerelease` allows whether to use Prerelease `PowerShell` modules or not.

#### Settings

These are passed to the `DSC resource`,[^2] representing things like:

1. Enable Developer Mode?
2. Apply a registry key?
3. Apply a particular network setting?

### Dependencies

The `dependsOn` field determines whether a certain [assertion](#assertions) or [resource](#resources) should be complete before performing a task.

## References

- [Winget configuration - Microsoft learn](https://learn.microsoft.com/en-us/windows/package-manager/configuration/create).

[^1]: Read more about [[semantic versioning]].
[^2]: Read about [DSC resource](https://learn.microsoft.com/en-us/powershell/dsc/concepts/resources?view=dsc-2.0).