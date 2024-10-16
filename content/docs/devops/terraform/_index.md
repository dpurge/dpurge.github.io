---
title: Terraform
bookCollapseSection: true
---

Terraform can provision infratsructure on public and private clouds.

Generic formats:

```tf
provider "{name}" { ...}

variable "{name}" { ... }

data "{provider}_{type}" "{name}" { ... }

resource "{provider}_{type}" "{name}" { ... }

output "{name}" { ... }
```

Reference formats:

```tf
var.{name}

data.{provider}_{type}.{name}.{attribute}
```
