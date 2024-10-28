# Appendix A - WebLOAD Analytics File System Structure



The WebLOAD Analytics file structure consists of system files, database files, log files, and files containing templates and template elements. The table below describes the WebLOAD file structure and its contents. The folders listed in the table below are located in the <WebLOAD directory>\bin folder.  

| **Folder**                                 | **Description**                                              |
| ------------------------------------------ | ------------------------------------------------------------ |
| Configuration                              | This folder is a WebLOAD Analytics system  folder.  This folder should only be  modified by qualified RadView technicians. |
| Database                                   | This folder contains the batch files required for the installation  and deployment of the WebLOAD Analytics Load Session Repository. |
| Gallery                                    | This folder contains all  WebLOAD Analytics templates. Each  template has its own folder containing a template JRXML file and a Jasper file.  Each template category  contains the Subreports  subdirectory. |
| Gallery\[Category]                         | A Category folder can be a group of templates, such as Pages Analysis  or any one of the following special categories:   Portfolios.   _Master Templates.   _System Templates. |
| Gallery\[Category]\ [Template]             | A Template folder exists  for every template in WebLOAD Analytics, such as Load Size Summary or HTTP  Responses.  A template consists of the following files:   .jrxml – JasperReports template file. Defines static templates structure,  can be edited using iReport. See[ *Using JasperSoft iReport* ](#_bookmark73)on page [61](#_bookmark73))   .jasper –  JasperReports compiled report. Generated automatically from .jrxml   .system.xml –  Defines a system defined interactive report.   .user.xml – Stores user defined settings, when using Save Chart As Template.   systemChart.xml – Stores graph configuration (such as colors, line  types, etc.)  userChart.xml – Stores user graph configuration. |
| Gallery\[Category]\  [Template]\SUBREPORTS | Some static Template folders contain additional .jrxml  subreports in  this folder, and their compiled .jasper files. |
| Gallery\[Category]\  [Template]\Resources  | Some Template folders contain this folder, which  contains the static graphical elements used by the template, including icons,  images, and logos. |
| Gallery\Portfolios                         | This category contains all the [Portfolio]  folders.         |
| Gallery\Portfolios\ [Portfolio]            | A Portfolio folder exists for every portfolio in WebLOAD Analytics,  such as Summary Report and Extended Summary Report.  This folder contains a .portfolio file, which is an XML file specifying the  templates included in the portfolio. |
| Gallery\  _Master  Templates               | This category is intended for advanced  users and cannot be accessed from WebLOAD Analytics.  The category contains the  master templates used by charts and reports. The master template of a report  defines the report appearance. The master template of a chart is used in  conjunction with the template to define the appearance of the chart. RadView  recommends that only advanced users should modify these templates.  When  you add a master template, it is available for selection in the Preferences window  (for more information, see [*Defining Your Analytics Preferences*   ](#_bookmark81)on  page [67](#_bookmark81)). |
| Gallery\  _System Templates                | This category is intended  for advanced users and cannot be accessed from WebLOAD Analytics.  The category contains  system templates that are references by other templates. For example, all  reports that are based on interactive reports reference a template in this  directory. |
| Plugins                                    | This folder is a WebLOAD Analytics system folder.  This folder should only be  modified by qualified RadView technicians. |
| Workspace                                  | This folder is created the first time that WebLOAD Analytics is  opened. It contains internal state persistence information. |

