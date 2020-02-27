<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html> 
      <body>
        <ul>
        <xsl:apply-templates/>
        </ul>
      </body>
    </html>
  </xsl:template>
  
  <xsl:template match="index">
    <xsl:for-each select="problem">
        <li><a href='{@href}' target="_PARENT" ><xsl:value-of select="@title"/></a></li>
    </xsl:for-each>
  </xsl:template>
  
</xsl:stylesheet>