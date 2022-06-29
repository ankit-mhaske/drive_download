package com.intent;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

public class Next extends Activity{

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		Button b1;
		// TODO Auto-generated method stub
		super.onCreate(savedInstanceState);
		setContentView(R.layout.next);
		b1=(Button)findViewById(R.id.button1);
		
		b1.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View arg0) {
				// TODO Auto-generated method stub
				Intent i=new Intent(Next.this,IntentActivity.class);
				startActivity(i);
			}
		});
	}
	
	

}
