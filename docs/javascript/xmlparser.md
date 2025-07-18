# XML Parser Object

 

WebLOAD provides an embedded, third-party XML parser object to improve the multi-platform support for XML parsing within the WebLOAD environment. The XML parser object can be used instead of MSXML and Java XML parsing, resulting in lower memory consumption and increased performance during load testing.

 

The XML parser object can be used to reference any element in an XML document. For example, you can use the XML parser object to generate an Excel file containing the desired details of a specified element. WebLOAD uses the Open Source Xerces XML parser (see [https://xerces.apache.org/xerces-c/](https://xerces.apache.org/xerces-c/)).

 

The XML parser object is instanced as follows:

`xmlObject = new XMLParserObject();`

 
The `parse()` method, not exposed by the original XML parser, is exposed by WebLOAD. This method is identical to the `parseURI()` method, except that it receives an XML string instead of a URI. The following sections provide lists of exposed methods and properties as well as a detailed example of the implementation of the XML parser object.


## Methods

 The following table lists the XML parser object methods exposed by WebLOAD.

 

| **Object**       | **Method  Name**                                             |
| ---------------- | ------------------------------------------------------------ |
| xmlparser        | <br>- parseURI  <br>- parse  <br>- resetDocumentPool  <br>- release  <br>- setFeature  <br>- getFeature  <br>- canSetFeature  <br>- load  <br>- loadXML |
| xmlAttr          | <br>- getName  <br>- getValue  <br>- setValue  <br>- getOwnerElement  <br>- getSpecified |
| xmlCharacterData | <br>- getData  <br>- getLength  <br>- appendData  <br>- setData  <br>- substringData  <br>- deleteData  <br>- insertData  <br>- replaceData |
| xmlDocument      | <br>- createElement  <br>- getElementById  <br>- getDocumentElement  <br>- getElementsByTagName  <br>- createTextNode  <br>- createDocumentFragment  <br>- getDoctype  <br>- createComment  <br>- createCDATAsection  <br>- createAttribute  <br>- createEntityReference  <br>- createProcessingInstruction  <br>- createElementNS  <br>- createAttributeNS  <br>- getElementsByTagNameNS  <br>- importNode |
| xmlDocumentType  | <br>- getName  <br>- getPublicId  <br>- getSystemId  <br>- getInternalSubset  <br>- getEntities  <br>- getNotations |
| xmlElement       | <br>- getElementsByTagName  <br>- getElementsByTagNameNS  <br>- getAttribute  <br>- getAttributeNS  <br>- getAttributeNode  <br>- getAttributeNodeNS  <br>- setAttributeNode  <br>- setAttributeNodeNS  <br>- getTagName  <br>- hasAttribute  <br>- hasAttributeNS  <br>- removeAttribute  <br>- removeAttributeNS  <br>- setAttribute  <br>- setAttributeNS  <br>- removeAttributeNode |
| xmlEntity        | <br>- getPublicId  <br>- getSystemId  <br>- getNotationName        |
| xmlnamednodemap  | <br>- getLength  <br>- getNamedItem  <br>- removeNamedItem  <br>- getNamedItemNS  <br>- removeNamedItemNS  <br>- setNamedItem  <br>- setNamedItemNS  <br>- item |
| xmlnode          | <br>- getNodeName  <br>- getNodeValue  <br>- getNodeType  <br>- getParentNode  <br>- getFirstChild  <br>- getLastChild  <br>- getPreviousSibling  <br>- getNextSibling  <br>- getChildNodes  <br>- getAttributes  <br>- getOwnerDocument  <br>- getNamespaceURI  <br>- getPrefix  <br>- getLocalName  <br>- hasChildNodes  <br>- hasAttributes  <br>- normalize  <br>- release  <br>- removeChild  <br>- appendChild  <br>- insertBefore  <br>- setNodeValue  <br>- setPrefix  <br>- isSupported |
| xmlnodelist      | <br>- Item  <br>- getLength                                      |
| xmlNotation      | <br>- getPublicId  <br>- getSystemId  <br>- xmlProcessingInstruction  <br>- getTarget  <br>- getData  <br>- setData |

 

 

 



## Properties

 The following table lists the XML parser object properties exposed by WebLOAD.

| **Object**               | **Property  Name**                                           |
| ------------------------ | ------------------------------------------------------------ |
| xmlAttr                  | <br>- name  <br>- value                                          |
| xmlCharacterData         | <br>- length  <br>- data                                         |
| xmlDocument              | <br>- documentElement                                          |
| xmlElement               | <br>- tagName                                                  |
| xmlnode                  | <br>- nodeName  <br>- attributes  <br>- childNodes  <br>- firstChild  <br>- lastChild  <br>- namespaceURI  <br>- nextSibling  <br>- nodeType  <br>- nodeValue  <br>- ownerDocument  <br>- parentNode  <br>- prefix  <br>- previousSibling  <br>- nodeTypeString  <br>- xml |
| xmlnodelist              | <br>- length                                                   |
| xmlProcessingInstruction | <br>- target  <br>- Data                                         |



 

## Example

The following is an example of the use of the XML parser object:

```javascript
{
//Create the XML parser object (xerces-c parser) 
xmlObject = new XMLParserObject();

//Parse the xml file from the specified path 
xmlDoc = xmlObject.parseURI("C:\\xml_file.xml");

//Retrieve the first node with the “NODE5” tag
domNode = xmlDoc.getElementsByTagName("NODE5").item(0);

//Retrieve the node's type 
nodeType = domNode.getNodeType();

//Retrieve the node's parent
nodeParent = domNode.getParentNode().getNodeName();

//Retrieve the number of child nodes
numOfChilds = domNode.getChildNodes().getLength();

//Create a new element
newNode1 = xmlDoc.createElement("NEW_NODE1");

//Insert the new element into DOM 
domNode1.insertBefore(newNode1, domNode);

}
```
