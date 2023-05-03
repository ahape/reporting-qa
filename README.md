
PRINT PREVIEW TESTS
===================

Toggle Sort Options
-------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103826581#report/3842/c89ff976-602d-45dd-a3a6-5b2e2c890c54)
  * Load the report
  * Click print preview
  * Expected -> "sort by" and "only show" record count checkboxes should be checked
  * Toggle both checkboxes to be unchecked
  * Expected -> report should render normally

Drill From Summary To Detail
----------------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103639426#report/3842/4dfc02f0-36d3-4b63-b694-702eb9874e1e)
  * Load the report
  * Click print preview
  * On the print preview page, click on one of the rows
  * Expected -> should open a new tab with a detail report

Title Shows Filter Rtw
----------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103204197#report/3842/cf34688e-00a2-4338-8db9-21ea86045149)
  * Load the report
  * Click print preview
  * Expected -> title information shows "recent time window" time filter, as well as the report table looks the same on both pages

Title Shows Filter Detail
-------------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103750425#report/3842/907a4d8d-1bdd-4faf-87f0-3959bbfce283)
  * Load the report
  * Click print preview
  * Expected -> title information shows the correct description of the "call minutes" (fact) filter set on the report
  * Expected -> the report on the print preview page should load instantaneously because it was seeded by data from the report page

Title Shows Filter Matches
--------------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230427221131472541&_qa=20230503003103554847#report/3842/10912a53-8ab8-4ac6-a0c8-b8d08777ecfe)
  * Load the report
  * Click print preview
  * Expected -> title information shows the correct description of the "caller ID starts with" (detail dimension) filter set on the report

Title Shows Filter Selected
---------------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103999209#report/3842/8d51f1e9-e263-405e-94ce-c89ef075261a)
  * Load the report
  * Click print preview
  * Expected -> title information shows the correct description of the "party name" filter set on the report

Title Shows Filter Proxy
------------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103821052#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
  * Load the report
  * Click print preview
  * Expected -> title information shows the correct description of the "party name by workgroup membership" filter set on the report

Title Shows Filter Range
------------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103112686#report/3842/4dfc02f0-36d3-4b63-b694-702eb9874e1e)
  * Load the report
  * Click print preview
  * Expected -> title information shows the time range, but doesn't show the "range" information (since it is redundant to the time range itself)

C2G
---
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103189664#report/3842/ff8b70b5-710c-4fc1-a2fe-a1f94515e0f0)
  * Load the report
  * Click print preview
  * On the print preview page, click on the green report cell
  * Expected -> should load C2G

From Dashboard Detail
---------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/DashboardDetail.aspx?tabid=912b9658-acd4-4ead-8ec2-debb18b8fb81&chartid=graph4&_qa=20230503003103543672)
  * Load the dashboard detail
  * Click print preview
  * Expected -> everything look normal

Basic
-----
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103769891#report/3842/4a4dffc2-b9be-4d51-b421-1270f726579e)
  * Load the report
  * Click print preview
  * Expected -> title information shows "relative" time filter, as well as the report table looks the same on both pages
  * Expected -> The company logo should appear on top of the VAR logo in the upper right hand corner
  * Expected -> the report on the print preview page should load instantaneously because it was seeded by data from the report page

Otfa
----
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230427221131472541&_qa=202305030031034706#report/3842/e90f0da4-2f0d-4adb-ad44-a956636d9157)
  * Load the report
  * Click print preview
  * Expected -> the OTFA report table should look the same on both pages

Fetch New Data
--------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103649840#report/3842/c89ff976-602d-45dd-a3a6-5b2e2c890c54)
  * Load the report
  * Click print preview
  * Once print preview loads, close the reports page
  * Refresh the print preview page
  * Expected -> print preview page should run a detail query, because it can't access the source page's data anymore


EXPORTING TESTS
===============

Print Preview Summary To Detail
-------------------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103383775#report/3842/4dfc02f0-36d3-4b63-b694-702eb9874e1e)
  * Load the report
  * Click print preview
  * Click on the cell that says "Jim Lewis"
  * Load the detail report
  * Expected -> detail report looks normal

Drill From Summary To Detail
----------------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103778237#report/3842/4dfc02f0-36d3-4b63-b694-702eb9874e1e)
  * Load the report
  * Click on the cell that says "Jim Lewis"
  * Load the detail report
  * Expected -> there should be a filter for "Jim Lewis", and when hovering over it, it should say "This was added from drilling into a summary report cell"
  * Expected -> detail should show as many records as were represented by the summary report aggregation
  * Expected -> detail report should be titled the same as the summary, except with "(detail)" tacked onto the end of it

Export Pdf Landscape
--------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103132770#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
  * Load the report
  * Click export
  * Expected -> the selections should be saved from last time (PDF / Portrait)
  * Select PDF, then select Landscape, then click EXPORT
  * Once the export finishes, open the file
  * Expected -> file should look the same as the report, and be rendered as a PDF in landscape orientation

Save Export Preferences
-----------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103276400#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
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

Basic Report Export
-------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103710918#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
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

Export Csv Formatted
--------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103675472#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
  * Load the report
  * Click export, then select CSV, then select Formatted, then click EXPORT
  * Once the export finishes, open the file
  * Expected -> file should look the same as the report, and be rendered as CSV, with times formatted XX:XX:XX and percentages rendered with the percent sign (%)

Export Csv Unformatted
----------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103347765#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
  * Load the report
  * Click export, then select CSV, then select Unformatted, then click EXPORT
  * Once the export finishes, open the file
  * Expected -> file should look the same as the report, and be rendered as CSV, with all values rendered as decimals

Export Excel
------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/Reports.aspx?_qa=20230503003103966347#report/3842/c4d24ef0-4900-4a22-b6c4-da8cb19b3823)
  * Load the report
  * Click export, then select Excel, then click EXPORT
  * Once the export finishes, open the file
  * Expected -> file should look the same as the report, and be rendered as XLSX

Save Dashboard Detail As Report
-------------------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/DashboardDetail.aspx?tabid=912b9658-acd4-4ead-8ec2-debb18b8fb81&chartid=graph4&_qa=20230503003103243800)
  * Load the dashboard detail
  * Click "Save as Report"
  * Expected -> report table to look the same on both the Dashboard Detail and Reports page

Export Report From Dashboard Detail
-----------------------------------
  * [(link to test)](https://webapp.brightmetrics.com/UI-2/pages/DashboardDetail.aspx?tabid=912b9658-acd4-4ead-8ec2-debb18b8fb81&chartid=graph4&_qa=20230503003103141930)
  * Load the dashboard detail page
  * Once the page loads, click the "Export" button
  * Once the dialog opens, select "Export Report" (it should be the default selection), then select CSV as the format, then select Unformatted as the format style
  * Click EXPORT
  * Once the export finishes, open the file
  * Expected -> file should look the same as the report, and be rendered as XLSX

