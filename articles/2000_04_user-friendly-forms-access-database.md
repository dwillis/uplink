# User-friendly forms

**By David Herzog**
*Providence Journal*

One of the things I've learned in my few years on the *Providence Journal* investigative team is that for such a small state, Rhode Island breeds some big corruption cases. As the CAR specialist on the paper's I-team, one of my roles is to gather the data to help uncover wrongdoing and make sure other reporters can get to it easily.

Not everyone working on these investigations wants to learn how to query databases, so I've used Microsoft Access to create stand-alone programs that allow reporters to point and click their way to useful information.

Access provides all the tools to create these programs and enough power to accomplish everything you need without resorting to programming.

Before getting into the nuts and bolts of creating a program, it's necessary to understand how you can design forms to create screens for entering and querying data. That's what this article is about. Once you know how to create a form, it's easy to learn how to create a program.

Forms are the building blocks of the programs you create. You use the forms to design screens for your program, enter data into tables and query tables. Another issue of *Uplink* will carry the details of making forms work with other objects to create the program.

Nearly every investigation relies on a chronology to organize the story, so let's use one to get started.

For this lesson, I'm using an Access database file called apriltech.mdb, which you can download from the NICAR web site *http://www.nicar.org*. After downloading the file, open it in Access. (I'm using Access 97). You can open the Chronology table in design view to look at the fields and data types.

The simplest way to create a form is to let the Form Wizard do the work, then tweak the form manually. For this form we want to make these three modifications: (1) Create a button to close the form. (2) Create a "pick list" of story topics. (3) Create a toolbar with buttons to allow easy querying.

## Create form

Create the form by clicking on the Forms tab, then New. Pick Form Wizard, then select the Chronology table from the pick list below. Click Ok. As you click the Next buttons, the Form Wizard will walk you through the steps of creating a form. Select all the fields, except for Edate, which Access will fill in automatically. Then, pick Columnar layout and pick a style. Finish and the wizard displays the form. Now you're ready to modify the form.

## Close button

Let's start with the close button. First go into the form's design view by clicking on the Design View button at the upper left (hint: it looks like a square and pencil). Make room for the button by pulling the Form Footer rule down. Then click on the command button in the tool box (if you put your cursor over each button, Access will tell you the name of each one) and click on the form.

The Command Button Wizard appears. In the Categories box pick Form Operations. In the Actions box, pick Close Form. Click on next and choose a button style. Click Next, then Finish. Go back to the form view and save the changes to your form. Click on the close button to make sure it works (you have to be in Form view).

## Pick List

Next, we'll add a pick list that contains pre-defined story topics. Return to the form's design view, select the topic field and delete. Click on the combo box button in the toolbar and then click on the form, where the topic field was. The Combo Box Wizard starts.

Select "I will type in the values that I want" and click on Next. Under Col1 type the story topics: Bribery, Sedition and Mutiny, using the Tab key to create a new line for each word. Then click Next.

In the next step, click Store that value in this field and select Topic from the pick list and click on Next. Now type a label for the pick list: "Topic" and click Finish.

Switch to the form view and you see that the Topic combo box has a pick list with your story topics.

## Entering data

Now try entering data into your form and use the Tab key to move through the fields. (If the cursor skips over the Topic field: Go back into Design View, right click on the form background and select Tab Order from the pop-up menu. Click Auto Order and Access creates a tab order based on the placement of the fields on the form. Click OK and go back to Form View.)

If you need to adjust any of the field widths or placement of field labels, you can do that in Design View. Finish adding records so you have a dozen or so for querying.

## Creating toolbar

To make things easy for users, we'll create a toolbar that will step users through queries using this form. Go back to Design View and select View–Toolbars–Customize from the menu.

In the Customize box click New and call your toolbar E-Z Query. A blank toolbar appears. Now we need to add buttons that will run the queries. In the Customize box, click the commands tab to access the available buttons. In the Categories box select Records. Then, drag and drop these three command buttons from the right onto the blank toolbar: Filter by form, Apply Filter and Remove Filter/Sort.

Since these buttons won't make sense to your users, we will create text buttons. Right click on the first button on the toolbar (while still in Design View) and in the text box that appears in the pop-up menu, type (1) Define query. Then click Text Only (Always) in the pop-up menu. Change the next two buttons to (2) Run query and (3) Show all.

Now we will make sure the toolbar appears with the form. Go back to the Customize box and click the Toolbars tab. Select E-Z Query and click the Properties button. Under Toolbar type, pick Toolbar. Under Docking, pick Allow any. With these settings, you'll be able to move the toolbar under the toolbars at the top of the Access window and make it look like a menu bar.

Attach the toolbar to the form by modifying the form's properties. To open the properties box, left click the form select box (it's the square to the immediate left of the ruler that runs from left to right) then right click to get the pop-up menu. Select Properties, then the Other tab. In the Toolbar field, pick E-Z Query, then close the Properties box.

## Ready to go

Save your database and get ready to query using the 1-2-3 method. Click the (1) Define Query button and you'll get a blank to enter query parameters. Let's look at records having to do with the Bribery story. Go to the Topic pick list and select bribery. Then click on the (2) Run query button to select just those records. At the bottom of the form, you will see how many records were selected. After looking at your records, pick (3) Show all to remove the filter. You can run queries on any of the fields and use Access' wildcards.

That's all you have to do to make data mining easy for other reporters. In the next article, we'll put together a stand-alone program that will make it even easier for others to get information out of your data.

David Herzog can be reached at the *Providence Journal*.
