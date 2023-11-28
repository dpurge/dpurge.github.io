# Java on MacOS

Install with homebrew:

```sh
brew search java
brew info java
brew install java
sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
```

Check:

```sh
ls -lsah /Library/Java/JavaVirtualMachines/
java -version
/usr/libexec/java_home -V
```

Setup `JAVA_HOME` in `~/.zshenv`:

```sh
export JAVA_HOME=$(/usr/libexec/java_home -v"21.0.1")
```

Refresh shell: `source ~/.zshenv`

Install Maven:

```sh
brew install maven
mvn -version
brew list maven
```

Settings are in `/opt/homebrew/opt/maven/libexec/conf/settings.xml`.

To upgrade or uninstall:

```sh
brew upgrade maven
brew uninstall maven
```

Install Java 8:

```sh
brew search openjdk
brew install openjdk@8
# Cannot install - it requires x86_64 architecture
```