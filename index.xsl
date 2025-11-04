<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html> 
      <head>
        <style>
          body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
            margin: 0;
            padding: 24px;
            background-color: transparent;
            color: #333;
            line-height: 1.6;
          }
          
          ul {
            list-style: none;
            padding: 0;
            margin: 0;
          }
          
          li {
            margin: 0;
            padding: 0;
            border-bottom: 1px solid #f0f0f0;
          }
          
          li:last-child {
            border-bottom: none;
          }
          
          a {
            display: block;
            padding: 12px 16px;
            color: #0D5257;
            text-decoration: none;
            font-size: 15px;
            transition: all 0.2s ease;
            border-left: 3px solid transparent;
          }
          
          a:hover {
            background-color: #f8f9fa;
            border-left-color: #0D5257;
            padding-left: 20px;
          }
          
          a:visited {
            color: #0D5257;
          }
        </style>
      </head>
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