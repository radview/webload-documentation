# WebLOAD-supported XML DOM Interfaces

 

WebLOAD supports the following XML DOM Document Interfaces:

- XML Document Interface

- Node Interface

- Node List Interface

- NamedNodeMap Interface

- ParseError Interface

- Implementation Interface

- XML Parser Interface


The tables in this appendix list the properties and methods of the interfaces supported by WebLOAD.

 

## XML Document Interface Properties

| **Property**       | **Description**                                              |
| ------------------ | ------------------------------------------------------------ |
| doctype            | A read-only property that  gets the node for the DTD specified for the document. If no DTD was  specified, null is returned. |
| documentElement    | A read/write property that  gets/sets the root node of the document. |
| implementation     | A read-only property that  returns the implementation interface for this document. |
| parseError         | A read-only property that  provides an object that summarizes the last parsing error encountered. |
| preserveWhitespace | A read-write property that informs the  parser whether the default mode of processing is to preserve whitespace or  not. The default value of this property is false. |
| readyState         | A read-only property  indicating the status of instantiating the XML processor and document  download. The value of the  readyState property is summarized in the table. |
| resolveExternals   | A read-write property that informs the parser that  resolvable namespaces (a namespaces URI that begin with an “x- schema:” prefix), DTD external  subsets, and external entity references should be resolved at parse time. |
| url                | A read-only property that returns the  canonicalized URL for the XML document specified in the last call to load(). |
| validateOnParse    | A read/write property that  turns validation on at parse time if the value of bool is true, off if validate is false. |



## XML Document Interface Methods

| **Method**                                   | **Description**                                              |
| -------------------------------------------- | ------------------------------------------------------------ |
| abort()                                      | Aborts an asynchronous download in  progress.                |
| createAttribute(name)                        | Creates a node of type ATTRIBUTE with the  name supplied.    |
| CreateCDATASection  (data)                   | Creates a node of type CDATA_SECTION with  nodeValue set to data. |
| createComment(data)                          | Creates a node of type  COMMENT with nodeValue set to data.  |
| createDocumentFragment                       | Creates a node of type  DOCUMENT_FRAGMENT in the context of the current document. |
| createElement(tagName)                       | Creates a node of type ELEMENT with the  nodeName of tagName. |
| createEntityReference(name)                  | Creates a node of type  ENTITY_REFERENCE where name is the name of the entity referenced. |
| CreateNode(type, name, namespaceURI)         | Creates a node of the type  specified in the context of the current document. Allows nodes to be created  as a specified namespace. |
| CreateProcessing  Instruction (target, data) | Creates a node of type  PROCESSING_INSTRUCTION with the target specified and nodeValue set to data. |
| createTextNode(data)                         | Creates a node of type TEXT with nodeValue  set to data.     |
| GetElementsByTagName  (tagname)              | Returns a collection of  all descendent Element nodes with a given tagName. |
| load(url)                                    | Loads an XML document from  the location specified by the url. If the url cannot be resolved or accessed or does not  reference an XML document, the documentElement is set to null and an error is  returned. Returns a Boolean. |
| loadXML(xmlstring)                           | Loads an XML document using the supplied string.  xmlstring can be an entire XML document or a  well-formed fragment. If the XML within xmlstring  cannot be loaded, the documentElement is set to null and an error is  returned. |
| NodeFromID(idstring)                         | Returns the node that has an ID attribute  with the value corresponding to idString. |
| Save()                                       | Serialize the XML. The  parameter can be a filename, an ASP response, an XML Document, or any other  COM object that supports Istream, IpersistStream, or IpersistStreamInit. |

 

 

  

## Node Interface Properties

| **Property**    | **Description**                                              |
| --------------- | ------------------------------------------------------------ |
| attributes      | A read-only property that returns a  NamedNodeMap containing attributes for this node. |
| BaseName        | A read-only property that  returns the right-hand side of a namespace qualified name. For example, yyy for the element <xxx:yyy>. BaseName must always return a non-empty string. |
| childNode       | A read-only property that returns a NodeList  containing all children of the node. |
| DataType        | A read-write property that indicates the node  type.         |
| Definition      | A read-only property whose value is the  node that contains the definition for this node. |
| FirstChild      | A read-only property that  returns the first child node. If the node has no children, firstChild  returns null. |
| LastChild       | A read-only property that  returns the last child node. If the node has no children, lastChild  returns null. |
| NextSibling     | A read-only property that  returns the node immediately following this node in the children of this  node’s parent. Returns null if no such node exists. |
| NamespaceURI    | A read-only property that  returns the URI for the namespace (the uuu portion of the namespace declaration xmlns:nnn=“uuu”). If there is no namespace on the node that is  defined within the context of the document, ““ is returned. |
| NodeName        | A read-only property indicating the name of  the node.       |
| NodeType        | A read-only property indicating the type of  node.           |
| NodeTypeString  | Returns the node type in string form.                        |
| NodeTypedValue  | A read/write property for the typed value of the  node.      |
| NodeValue       | A read/write property for the value of the node.             |
| OwnerDocument   | A property that indicates  the document to which the node belongs or when the node is removed from a  document. |
| parentNode      | A read-only property that provides a  pointer to the parent. |
| parsed          | A read-only property that  indicates that this node and all of its descendants have been parsed and  instantiated. This is used in conjunction with asynchronous access to the  document. |
| prefix          | A read-only property that  returns the prefix specified on the element, attribute of entity reference.  For example, xxx for  the element  <xxx:yyy>. If there is no  prefix specified, ““ is returned. |
| previousSibling | A read-only property that  returns the node immediately preceding this node in the children of this  node’s parent. Returns null if no such node exists. |
| specified       | A read-only property  indicating the node was specified directly in the XML source and not implied  by the DTD schema. |
| text            | A string representing the  content of the element and all descendents. For example “content of tag” in  <sometag size=34> content of  tag  </sometag>. |
| xml             | A read-only property that  returns the XML representation of the node and all its descendants as a  string. |



 

 

## Node Interface Methods

| **Method**                                  | **Description**                                              |
| ------------------------------------------- | ------------------------------------------------------------ |
| appendChild(newChild)                       | A method to append newChild as the last child of this node.  |
| cloneNode(deep)                             | A method to create a new  node that is an exact clone (same name, same attributes) as this node. When  deep is false, only the node and attributes without its children are cloned.  When deep is true, the node and all its descendants are cloned. |
| hasChildNodes()                             | A method that indicates  whether the node has children.      |
| InsertBefore  (newChild, oldChild)          | A method to insert newChild  as a child of  this node. oldChild is returned. oldNode must  be a child node of the element, otherwise an error is returned. If newChild  is null, the oldChild  is removed. |
| removeChild(child)                          | A method to remove a childNode from a node. If childNode is not a child of the  node, an error is returned. |
| ReplaceChild  (newChild, oldChild)          | A method to replace oldChild with newChild as a child of this node. |
| selectNodes(query)                          | Returns a NodeList containing the results of  the query indicated by query, using the current node as the query context. If  no nodes match the query, an empty NodeList is returned. If there is an error in the query  string, the DOM error reporting is used. |
| SelectSingleNode  (query)                   | Returns a single node that  is the first node in the NodeList returned from the query,  using the current node as the query context. If no nodes match the query,  null is returned. If there is an error in the query string, an error is  returned. |
| TransformNode (stylesheetDOMNode)           | Returns the results of  processing the source DOMNode and its children with the  stylesheet indicated by stylesheetDOMNode. The source defines the  entire context on which the stylesheet operates, so ancestor or id navigation  outside of the scope is not allowed. The stylesheet parameter must be either  a DOM Document node, in which case the document is assumed to be an ASL stylesheet,  or a DOM Node in the xsl namespace, in which case this node is treated as a standalone. |
| TransformNodeToObject  (stylesheet, Object) | Sends the results of the transform to the  requested object, either in IStream or a DOM Document. |



 



## Node List Interface

| **Property** | **Description**                                              |
| ------------ | ------------------------------------------------------------ |
| length       | The number of nodes in the  NodeList. The length of the list will change dynamically as children or  attributes are added/deleted from the element. |
| nextNode     | Returns the next node in  the NodeList based  on the current node. |
| item(index)  | Returns the node in the NodeList with the specified index.   |
| reset()      | Returns the iterator to the uninstantiated  state; that is, before the first node in the NodeList. |



## NamedNodeMap Interface

| **Property**                                  | **Description**                                              |
| --------------------------------------------- | ------------------------------------------------------------ |
| length                                        | The number of nodes in the  NamedNodeMap. The length of the list will change dynamically  as children or attributes are added/deleted from the element. |
| getNamedItem(name)                            | Returns the node  corresponding to the attribute with name. If name is not an attribute, null  is returned. |
| GetQualifiedItem  (baseName, namespaceURI)    | Allows the specification  of a qualifying namespaceURI to access a namespace  qualified attribute. It returns the node corresponding to the attribute with baseName  in the  namespace specified by nameSpaceURI. If the qualified name (baseName+nameSpaceURI) is not an attribute,  null is returned. |
| item(index)                                   | Returns the node in the NameNodeMap  with the  specified index. If the index is greater than the total number of nodes, null  is returned. If the index is less than zero, null is returned. |
| nextnode()                                    | Returns the next node in  the NodeList based  on the current node. |
| RemovedNamedItem (name)                       | Removes the attribute node  corresponding to name and returns the node. If name is not an attribute, null  is returned. |
| RemoveQualifiedItem (basename,  namespaceURI) | Removes the nameSpaceURI  qualified  attribute node corresponding to baseName and returns the node. If the qualified name is not  an attribute, null is returned. |
| reset()                                       | Returns the iterator to  the uninstantiated state; that is before the first node in the NodeList. |
| SetNamedItem (namedItem)                      | Adds the attribute Node  to the list.  If an attribute already exists with the same name as that specified by nodeName of DOMNode, the attribute is  replaced and the node is returned. Otherwise, Node is returned. |
|                                               |                                                              |

 

## ParseError Interface

| **Item**  | **Description**                                              |
| --------- | ------------------------------------------------------------ |
| errorcode | Returns the error code number in decimal.                    |
| filepos   | Returns the absolute file  position where the error occurred. |
| line      | Returns number of the line containing the  error.            |
| linepos   | Returns the character  position where the error occurred.    |
| reason    | Returns the reason for the error.                            |
| srcText   | Returns the full text of the line  containing the error.     |
| url       | Returns the URL of the XML  file containing the error.       |

 



## Implementation Interface

| **Item**                       | **Description**                                              |
| ------------------------------ | ------------------------------------------------------------ |
| HasFeature  (feature, version) | The method returns true if the specified  version of the parser supports the specified feature. In Level 1, “1.0” is  the only valid version value. |



 
