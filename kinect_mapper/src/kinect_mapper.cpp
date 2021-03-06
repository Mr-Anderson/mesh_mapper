/*******************************************************************************
 * @file kinect_mapper.cpp
 * @author James Anderson <jra798>
 * @version 1.0
 * @brief main file to exstract a mesh from RGBD camera
 ******************************************************************************/
 #include "kinect_mapper.h"
 
/***********************************************************
* @fn imageCallback(const sensor_msgs::ImageConstPtr& msg)
* @brief preforms sobel edge detection on image
* @pre takes in a ros message of a raw or cv image
* @post publishes a CV_32FC1 image using cv_bridge
* @param takes in a ros message of a raw or cv image 
***********************************************************/
void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
	//ROS_INFO("Edge_Detection: Image receieved");
	
	cv_bridge::CvImagePtr cv_ptr_src;
	
	//takes in the image
	
    try
    {
      cv_ptr_src = cv_bridge::toCvCopy(msg, "rgb8");
      
    }
    catch (cv_bridge::Exception& e)
    {
      ROS_ERROR("cv_bridge exception: %s", e.what());
      return;
    }
    
    //creates internal images
    cv::Mat sobel_x(cv_ptr_src->image.size(),CV_32FC1);
    cv::Mat sobel_y(cv_ptr_src->image.size(),CV_32FC1);
    cv::Mat sobel(cv_ptr_src->image.size(),CV_32FC1);
    cv::Mat laplace(cv_ptr_src->image.size(),CV_32FC1);
    cv::Mat canny(cv_ptr_src->image.size(),CV_32FC1);
    std::vector<cv::Mat> Chanels;
    cv::Mat out(cv_ptr_src->image.size(), CV_32FC1);
    cv_bridge::CvImage out_msg;
    
    //sets out to zeros so it can be added to 
    out = cv::Mat::zeros(cv_ptr_src->image.size(),CV_32FC1);
    
    int order;
    if(params.second_order)
    {
    	order = 5;
    	if(params.third_order)
    	{
    		order = 7;
    	}
    }
    else
    {
    	order = 3;
    }
    
    if(params.sobel)
    {
		//preforms x and y sobels
		cv::Sobel(cv_ptr_src->image, sobel_x, 3, 1, 0, order, .3);
		cv::Sobel(cv_ptr_src->image, sobel_y, 3, 0, 1, order , .3);
		
		sobel_x = cv::abs(sobel_x );
		sobel_y = cv::abs(sobel_y );
		
		//adds them together
		cv::add(sobel_x, sobel_y, sobel);
		
		sobel = sobel/pow(order,2);
		
		//splits into three chanels
		cv::split(sobel , Chanels);
		

		//ads the sqares of the chanels together
		for(int i = 0 ; i < 3; i++)
		{
			Chanels[i].convertTo(Chanels[i],CV_32FC1);
			cv::pow(Chanels[i] , 2 ,Chanels[i] );
		
			cv::addWeighted(Chanels[i], params.sobel_per_add/100 , out, (100-params.sobel_per_add)/100  ,1/3, out);

		} 
		
		//multiply by scaler
		out = out * (params.scaler_percent/100);
		
		//takes the square root to get the magnitude
		if(params.square_root)
		{	
			sqrt(out,out);
		}
    }
    
    if(params.laplace)
    {
    	cv::Laplacian(cv_ptr_src->image,laplace,3);
    	
    	//splits into three chanels
		cv::split(laplace , Chanels);
		

		//ads the sqares of the chanels together
		for(int i = 0 ; i < 3; i++)
		{
			Chanels[i].convertTo(Chanels[i],CV_32FC1);
			cv::pow(Chanels[i] , 2 ,Chanels[i] );
		
			cv::addWeighted(Chanels[i], params.laplace_per_add/100 , out, (100-params.laplace_per_add)/100 ,1/3, out);

		} 
		
		//multiply by scaler
		out = out * (params.scaler_percent/100);
		
		//takes the square root to get the magnitude
		if(params.square_root)
		{	
			sqrt(out,out);
		}
    }
    
    int canny_order;
    if(params.canny_second_order)
    {
    	canny_order = 5;
    	if(params.canny_third_order)
    	{
    		canny_order = 7;
    	}
    }
    else
    {
    	canny_order = 3;
    }
    
    if(params.canny)
    {
    
    	cv::split(cv_ptr_src->image , Chanels);
    	    	
   
		//ads the sqares of the chanels together
		for(int i = 0 ; i < 3; i++)
		{
			Chanels[i].convertTo(Chanels[i],CV_8UC1);
			
			cv::Canny(Chanels[i], Chanels[i], params.canny_thresh_1 , params.canny_thresh_2, canny_order);
			
			cv::pow(Chanels[i] , 2 ,Chanels[i] );
			
			Chanels[i].convertTo(Chanels[i],CV_32FC1);
			
			Chanels[i] = Chanels[i] * params.canny_val;
		
			cv::addWeighted(Chanels[i], params.canny_per_add/100 , out, (100-params.canny_per_add)/100 ,1/3, out);

		} 
		
		//multiply by scaler
		out = out * (params.scaler_percent/100);
		
		//takes the square root to get the magnitude
		if(params.square_root)
		{	
			sqrt(out,out);
		}

    }
    

    //changes it back to a cv image then publishes message
    out_msg.header = cv_ptr_src->header;
    out_msg.encoding = "32FC1";
    out_msg.image = out ;
    
    image_pub.publish(out_msg.toImageMsg());

}

/***********************************************************
* @fn setparamsCallback(const sensor_msgs::ImageConstPtr& msg)
* @brief callback for the reconfigure gui
* @pre has to have the setup for the reconfigure gui
* @post changes the parameters
***********************************************************/
void setparamsCallback(MST_Edge_Detection::Edge_Detection_ParamsConfig &config, uint32_t level)
{
  
  
  if(config.third_order && !config.second_order)
  {
    config.third_order = false; 
  }
  
  // set params
  params = config;
  
}


/***********************************************************
* @fn main(int argc, char **argv)
* @brief starts the Edge_Detection node
***********************************************************/
int main(int argc, char **argv)
{
    ros::init(argc, argv, "Edge_Detection");
    ros::NodeHandle n;
    image_transport::ImageTransport it(n);
    
    //setup dynamic reconfigure gui

    dynamic_reconfigure::Server<MST_Edge_Detection::Edge_Detection_ParamsConfig> srv;
    dynamic_reconfigure::Server<MST_Edge_Detection::Edge_Detection_ParamsConfig>::CallbackType f;
    f = boost::bind(&setparamsCallback, _1, _2);
    srv.setCallback(f);
    
    
    
    //get topic name
    topic = n.resolveName("image");

    //check to see if user has defined an image to subscribe to 
    if (topic == "/image") 
    {
        ROS_WARN("Edge_Detection: image has not been remapped! Typical command-line usage:\n"
                 "\t$ ./Edge_Detection image:=<image topic> [transport]");
    }
    

    image_sub = it.subscribe( topic , 1, imageCallback  );

    image_pub = it.advertise( "image_edges" , 5 );

    ros::spin();
    
    return 0;
}

