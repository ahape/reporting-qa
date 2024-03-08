
EXPORTING TESTS
===============

Basic Report Export
-------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_286368#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
* Load the report
* Click export
* Select PDF
* Select Portrait
* Change the title of the export to "TEST"
* Click EXPORT
* Once the export finishes, open the file (don't close the Export browser tab)
* Expected -> filename should be titled "TEST.pdf"
* Expected -> file should look the same as the report, and be rendered as a PDF in portrait orientation
* In the Export browser tab, click the link that says "click here to download manually"
* Expected -> Another file should download

Drill From Summary To Detail
----------------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_369865#report/3842/4dfc02f0-36d3-4b63-b694-702eb9874e1e)
* Load the report
* Click on the cell that says "Jim Lewis"
* Load the detail report
* Expected -> there should be a filter for "Jim Lewis", and when hovering over it, it should say "This was added from drilling into a summary report cell"
* Expected -> detail should show as many records as were represented by the summary report aggregation
* Expected -> detail report should be titled the same as the summary, except with "(detail)" tacked onto the end of it

Export Csv Formatted
--------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_356970#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
* Load the report
* Click export, then select CSV, then select Formatted, then click EXPORT
* Once the export finishes, open the file
* Expected -> file should look the same as the report, and be rendered as CSV, with times formatted XX:XX:XX and percentages rendered with the percent sign (%)

Export Csv Unformatted
----------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_124642#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
* Load the report
* Click export, then select CSV, then select Unformatted, then click EXPORT
* Once the export finishes, open the file
* Expected -> file should look the same as the report, and be rendered as CSV, with all values rendered as decimals

Export Excel
------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_616005#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
* Load the report
* Click export, then select Excel, then click EXPORT
* Once the export finishes, open the file
* Expected -> file should look the same as the report, and be rendered as XLSX

Export Pdf Landscape
--------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_182678#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
* Load the report
* Click export
* Expected -> the selections should be saved from last time (PDF / Portrait)
* Select PDF, then select Landscape, then click EXPORT
* Once the export finishes, open the file
* Expected -> file should look the same as the report, and be rendered as a PDF in landscape orientation

Export Report From Dashboard Detail
-----------------------------------
* [(link to test)](http://localhost:8080/UI-2/pages/DashboardDetail.aspx?tabid=912b9658-acd4-4ead-8ec2-debb18b8fb81&chartid=graph4&_qa=20240308101733_39748)
* Load the dashboard detail page
* Once the page loads, click the "Export" button
* Once the dialog opens, select "Export Report" (it should be the default selection), then select Excel as the format, then select Unformatted as the format style
* Click EXPORT
* Once the export finishes, open the file
* Expected -> file should look the same as the report, and be rendered as XLSX
* Expected -> the filename should be the same as the dashboard detail title

Print Preview Summary To Detail
-------------------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_9660#report/3842/4dfc02f0-36d3-4b63-b694-702eb9874e1e)
* Load the report
* Click print preview
* Click on the cell that says "Jim Lewis"
* Load the detail report
* Expected -> detail report looks normal

Save Dashboard Detail As Report
-------------------------------
* [(link to test)](http://localhost:8080/UI-2/pages/DashboardDetail.aspx?tabid=912b9658-acd4-4ead-8ec2-debb18b8fb81&chartid=graph4&_qa=20240308101733_349762)
* Load the dashboard detail
* Click "Save as Report"
* Expected -> report table to look the same on both the Dashboard Detail and Reports page
* Expected -> the report name should be the source chart name, and the report group should be the data source name

Save Export Preferences
-----------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_45782#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
* Load the report
* Click print preview
* Once the report loads, click "Export to Excel"
* Expected -> export dialog should appear with "Excel" auto-selected. Now close that dialog
* Click "Export to CSV"
* Expected -> export dialog should appear with "CSV" auto-selected. Now close that dialog
* Click "Export to PDF"
* Expected -> export dialog should appear with "PDF" auto-selected
* Click EXPORT
* Once the export finishes, open the file
* Expected -> file should look the same as the report, and be rendered as PDF

Xdata
-----
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_158785#report/1440768/dafe8675-6029-4adf-881c-3f909ef4a2de)
* Load the report
* Click on any drill-through cell
* Expected -> morevert menu prompts you for which data source to drill into
* Click on "Call Legs"
* Let the detail report load
* Expected -> everything looks normal

Xdata With Proxy Filter
-----------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_394886#report/1440768/33ea0098-814e-4304-83ca-02de797ad0f7)
* Load the report
* Click on the cell that says "Wednesday"
* Select "Call Legs" as the drill-through data source
* Expected -> for a brief moment, a detail query dialog should appear, then afterward, a new tab should open
* Expected -> the detail report should load normally


PRINT PREVIEW TESTS
===================

Basic
-----
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_483818#report/3842/4a4dffc2-b9be-4d51-b421-1270f726579e)
* Load the report
* Click print preview
* Expected -> title information shows "relative" time filter, as well as the report table looks the same on both pages
* Expected -> The company logo should appear on top of the VAR logo in the upper right hand corner
* Expected -> the report on the print preview page should load instantaneously because it was seeded by data from the report page

C2G
---
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_639953#report/3842/ff8b70b5-710c-4fc1-a2fe-a1f94515e0f0)
* Load the report
* Click print preview
* On the print preview page, click on the green report cell
* Expected -> should load C2G

Drill From Summary To Detail
----------------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_199767#report/3842/4dfc02f0-36d3-4b63-b694-702eb9874e1e)
* Load the report
* Click print preview
* On the print preview page, click on one of the rows
* Expected -> should open a new tab with a detail report

Fetch New Data
--------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_567877#report/3842/c89ff976-602d-45dd-a3a6-5b2e2c890c54)
* Load the report
* Click print preview
* Once print preview loads, close the reports page
* Refresh the print preview page
* Expected -> print preview page should run a detail query, because it can't access the source page's data anymore

From Dashboard Detail
---------------------
* [(link to test)](http://localhost:8080/UI-2/pages/DashboardDetail.aspx?tabid=912b9658-acd4-4ead-8ec2-debb18b8fb81&chartid=graph4&_qa=20240308101733_831296)
* Load the dashboard detail
* Click print preview
* Expected -> everything look normal

Otfa
----
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_523709#report/3842/e90f0da4-2f0d-4adb-ad44-a956636d9157)
* Load the report
* Click print preview
* Expected -> the OTFA report table should look the same on both pages

Title Shows Filter Detail
-------------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_665329#report/3842/907a4d8d-1bdd-4faf-87f0-3959bbfce283)
* Load the report
* Click print preview
* Expected -> title information shows the correct description of the "call minutes" (fact) filter set on the report
* Expected -> the report on the print preview page should load instantaneously because it was seeded by data from the report page

Title Shows Filter Matches
--------------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_908637#report/3842/10912a53-8ab8-4ac6-a0c8-b8d08777ecfe)
* Load the report
* Click print preview
* Expected -> title information shows the correct description of the "caller ID starts with" (detail dimension) filter set on the report

Title Shows Filter Proxy
------------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_254546#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
* Load the report
* Click print preview
* Expected -> title information shows the correct description of the "party name by workgroup membership" filter set on the report

Title Shows Filter Range
------------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_483464#report/3842/4dfc02f0-36d3-4b63-b694-702eb9874e1e)
* Load the report
* Click print preview
* Expected -> title information shows the time range, but doesn't show the "range" information (since it is redundant to the time range itself)

Title Shows Filter Rtw
----------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_581859#report/3842/cf34688e-00a2-4338-8db9-21ea86045149)
* Load the report
* Click print preview
* Expected -> title information shows "recent time window" time filter, as well as the report table looks the same on both pages

Title Shows Filter Selected
---------------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_193623#report/3842/8d51f1e9-e263-405e-94ce-c89ef075261a)
* Load the report
* Click print preview
* Expected -> title information shows the correct description of the "party name" filter set on the report

Toggle Sort Options
-------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_65851#report/3842/c89ff976-602d-45dd-a3a6-5b2e2c890c54)
* Load the report
* Click print preview
* Expected -> "sort by" and "only show" record count checkboxes should be checked
* Toggle both checkboxes to be unchecked
* Expected -> report should render normally

Xdata
-----
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_247516#report/1440768/dafe8675-6029-4adf-881c-3f909ef4a2de)
* Load the xdata report
* Click print preview
* Expected -> everything looks normal


REPORT-FIELD-EDITOR TESTS
=========================

Basic Detail
------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_274223#report/3842/10912a53-8ab8-4ac6-a0c8-b8d08777ecfe)
* Run the report
* In LAYOUT>Values, click the morevert on Call Minutes and select ADD THRESHOLD
* In "Alert Threshold Amount" type 3
* In "Warning Threshold Amount" type 1
* Click APPLY
* Expected -> All Call Minutes cells over 3 minutes should appear in red, and the cells that are less than 3 but greater than 1 should appear in yellow
* In LAYOUT>Values, click the morevert on Call Minutes and select EDIT THRESHOLD
* Change the Alert color to something else, then click APPLY
* Expected -> Red cells should change to the color chosen
* In LAYOUT>Values, click the morevert on Call Minutes and select EDIT THRESHOLD
* Click DELETE
* Expected -> All threshold coloring should disappear from report
* In LAYOUT>Columns, click the morevert on Call Reason and select ADD THRESHOLD
* Click "Click here to select values"
* Expected -> The MultipleSelect dialog should appear with a list of possible values
* Click on "Called", then click APPLY, then click APPLY again
* Expected -> All of the Call Reason fields should appear in the threshold coloring
* In LAYOUT>Values, drag the Call Minutes field into the Report Filters area
* Expected -> Should create a filter on Call Minutes
* Expected -> A filter icon should appear on the Call Minutes field in the Values section

Basic Summary
-------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_452544#report/3842/8d51f1e9-e263-405e-94ce-c89ef075261a)
* Collapse LAYOUT pane
* Expected -> collapses
* Expand LAYOUT pane
* Expected -> expands
* Expand FIELDS pane
* Collapse LAYOUT pane
* Expected -> LAYOUT and FIELDS collapse
* Expand FIELDS pane
* Drag a summary field from FIELDS>Available Dimensions onto LAYOUT>Rows
* Expected -> Should move from one container to another
* Expected -> Should re-render the report
* Add a field onto LAYOUT>Columns via dropdown ("Drag/Search Field Here")
* Expected -> Should remove field from Available Dimensions, and appear in Column
* Switch to Values tab in FIELDS pane
* Add a field onto Values via morevert
* Expected -> Field should not be in FIELDS>Available Values container
* Expected -> Field should be in LAYOUT>Values container
* Drag field from LAYOUT>Rows over FIELDS container
* Expected -> FIELDS container should have switched its active tab from Dimensions to Values
* Expected -> Field should disappear from Rows and appear in AD
* Remove a field from LAYOUT>Columns via morevert
* Expected -> Field should disappear from Columns and appear in AD
* Drag a field from Columns to Rows
* Expected -> Should work
* Expand field grouping Call Date_Grp
* Expected -> Should expand
* Drag field from Call Date_Grp onto report
* Collapse field grouping
* Drag field back into FIELDS>Available Dimensions
* Expected -> Field grouping should highlight, indicating something happened w/in it
* Expected -> If you expand the field grouping again, the field that you removed from the report should be present there
* With field grouping still expanded, resize browser window to make it tiny
* Scroll FIELDS>Available Dimensions section all the way to the bottom
* Expected -> Field grouping label should act as a sticky header and remain at the top of the container while scrolling
* Drag an Available Dimension all the way into Report Filters section
* Expected -> Filter area should have highlighted once the field was over the dropzone
* Try dragging an Available Value all the way into the Report Filters section
* Expected -> Shouldn't be allowed
* Hover over any field in FIELDS or LAYOUT
* Expected -> Should see tooltip
* Click the morevert on a field in Rows or Columns that doesn't have a filter set, and select ADD FILTER
* Expected -> Filter should appear in the Report Filters area
* Click the morevert on that same field you just added a filter to, and select REMOVE FILTER
* Expected -> Filter should be removed from the Report Filters area


REPORT RUNNING TESTS
====================

Cancel Detail Request
---------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_68698#report/1260804/0e578889-604a-40cc-a40c-8f0b646ed0e9)
* Open the developer tools, and view the Network tab
* Run the report (1)
* The moment the detail query dialog shows up, press cancel (while it says "Queuing up agent task") - This will attempt to abort the AJAX request that triggers the agent command - This will ALSO ensure that if the AJAX completes, we'll subsequently send an action=cancel
* Expected -> request is cancelled, a request is made to /Commands with action=cancel, and no more polls to /Commands are made
* Run the report (2)
* Once the detail query dialog shows up, wait until is says "Waiting for task to complete on agent", then press cancel
* Expected -> request is cancelled, a request is made to /Commands with action=cancel, and no more polls to /Commands are made
* Run the report (3)
* Then click on another page in the app sidebar
* Expected -> request is cancelled, a request is made to /Commands with action=cancel, and no more polls to /Commands are made
* Open up Fiddler, and capture traffic for your browser process
* Run the report (4)
* Close the browser tab
* Expected -> request is cancelled, a request is made to /Commands with action=cancel (can only be verified via Fiddler)


REPORT SAVING TESTS
===================

Detail From Scratch
-------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_823661#1440768/System)
* Click "Create new report"
* Select "User Activity"
* Click "Detail"
* Expected -> report appears blank, with a relative datetime filter applied
* Add a column to the report
* Add a value to the report
* Click "Run Report"
* Click "Save As"
* Enter a custom report grouping and name
* Expected -> the newly saved report is loaded, with the correct name and grouping
* Now go ahead and delete the report
* Expected -> it deletes

Summary From Scratch
--------------------
* [(link to test)](http://localhost:8080/UI-2/pages/Reports.aspx?_qa=20240308101733_996688#1440768/System)
* Click "Create new report"
* Select "User Activity"
* Click "Summary"
* Expected -> report appears blank, with a relative datetime filter applied
* Add a row to the report
* Add a value to the report
* Click "Save As"
* Enter a custom report grouping and name
* Expected -> the newly saved report is loaded, with the correct name and grouping
* Now go ahead and delete the report
* Expected -> it deletes

