package model;

public class MorphCategory {
	
	private String name;
	private String[] values;
	
	public MorphCategory(String name, String[] values) {
		super();
		this.name = name;
		this.values = values;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String[] getValues() {
		return values;
	}

	public void setValues(String[] values) {
		this.values = values;
	}
	
}
