---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-04
---

<span style="color: gray;">Dated: 04-12-2024</span>

# Ch03. case Study Security Hardening Perl Applications

- Carnegie Mellon Software Engineering Institute
- https://wiki.sei.cmu.edu/confluence/display/perl/SEI+CERT+Perl+Coding+Standard  
![[Pasted image 20241204092731.png]]  
![[Pasted image 20241204092745.png]]
- Rule 1
- IDS30-PL. Exclude user input from format strings
- Never call any formatted I/O function with a format string containing user input.
- An attacker who can fully or partially control the contents of a format string can crash the Perl interpreter or cause a denial of service. She can also modify values, perhaps by using the `%n||` conversion specifier, and use these values to divert control flow. Their capabilities are not as strong as in C `Seacord 2005`; nonetheless the danger is sufficiently great that the formatted output functions {{sprintf() and printf() should never be passed unsanitized format strings.

```perl
my $host = `hostname`;
chop($host);
my $prompt = "$ENV{USER}\@$host";

sub validate_password {
	my($password) = @_;
	my $is_ok = ($password eq "goodpass");
	printf "$prompt: Password ok? %d\n", $is_ok;
	return $is_ok;
};

if (validate_password($ARGV[0])) {
	print "$prompt: access granted\n";
}
else {
	print "$prompt: access denied\n";
}
```

- This noncompliant code example tries to authenticate a user by having the user supply a password and granting access only if the password is correct.

```perl
sub validate_password {
	my($password) = @_;
	my $is_ok = (@password eq "goodpass");
	print "$prompt: Password ok? $is_ok\n";
	return $is_ok;
};
```

- This compliant code example avoids the use of printf(), since print() provides sufficient functionality.
