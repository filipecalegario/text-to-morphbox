package main;

import java.util.ArrayList;

import model.MorphCategory;
import processing.core.PApplet;

public class PDFExportTest extends PApplet {

	float pdfWidth = 500.0f;
	float pdfHeight = 350.0f;
	ArrayList<MorphCategory> categories;

	public void settings() {
		float widthInPixels = pdfWidth / 0.353f;
		float heightInPixels = pdfHeight / 0.353f;
		size(round(widthInPixels), round(heightInPixels));
	}

	public void setup() {
		beginRecord(PDF, "output.pdf");
		categories = new ArrayList<>();
		String[] lines = loadStrings("input.txt");
		for (int i = 0; i < lines.length; i++) {
			String[] parts = lines[i].split(":");
			String categoryName = parts[0].trim();
			String[] values = parts[1].split(",");
			if(!categoryName.startsWith("#")) {
				categories.add(new MorphCategory(categoryName, values));
			}
			//			System.out.print("Category: " + categoryName + " = ");
			//			for (int j = 0; j < values.length; j++) {
			//				System.out.print("#"+values[j].trim()+"#");
			//			}
			//			System.out.println();
		}
		drawCategories();
		//noLoop();
	}

	private void drawCategories() {
		background(255);
		textSize(16);
		float cellHeight = this.height * 1.0f / categories.size() * 1.0f;
		int indexY = 0;
		float titleCellWidth = textWidth(calculateMaxTitleWidth()) + 10;
		for (MorphCategory morphCategory : categories) {
			float cellWidth = (this.width - titleCellWidth) * 1.0f / morphCategory.getValues().length * 1.0f;
			noFill();
			rect(0, indexY*cellHeight, titleCellWidth, cellHeight);
			fill(0);
			text(morphCategory.getName(), 5, (indexY*cellHeight)+cellHeight/2.0f);
			for (int i = 0; i < morphCategory.getValues().length; i++) {
				noFill();
				rect(titleCellWidth+i*cellWidth, indexY*cellHeight, cellWidth, cellHeight);
				fill(0);
				String label = morphCategory.getValues()[i];
				text(label, titleCellWidth+i*cellWidth + cellWidth/2.0f - textWidth(label)/2.0f, indexY*cellHeight+cellHeight/2.0f+5);
			}
			indexY++;
		}
	}

	private String calculateMaxTitleWidth() {
		String longestTitle = "";
		for (MorphCategory morphCategory : categories) {
			if(morphCategory.getName().length() > longestTitle.length()){
				longestTitle = morphCategory.getName().toString();
			}
		}
		return longestTitle;
	}

	public void draw() {
		//ellipse(mouseX, mouseY, 10, 10);
	}

	public void mousePressed() {
		endRecord();
		exit();
	} 

	public void keyPressed() {
		endRecord();
		exit();
	}
	static public void main(String[] passedArgs) {
		String[] appletArgs = new String[] { "main.PDFExportTest" };
		if (passedArgs != null) {
			PApplet.main(concat(appletArgs, passedArgs));
		} else {
			PApplet.main(appletArgs);
		}
	}
}
