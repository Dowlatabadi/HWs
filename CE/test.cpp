#include <iostream>
#include <vector>
#include <math.h> 
#include<tuple> // for tuple
#include <queue>
#include <limits>
using namespace std;
float get_rnd_ex(double mean=100){
        double result;
        // param = 2.73;
        float r = (1-((double) rand() / (RAND_MAX)));
        result = -log (r)*mean;
        return result;
}
vector<tuple<double, double>> update_due(vector<tuple<double, double>> q,double span){
for (int i = 0; i < q.size(); i++) {
  q[i]=tuple<float, float>(
      get<0>(q[i])-span
      ,get<1>(q[i]));
}

return q;
}
float get_rnd(double mean=10){
    float r = ((double) rand() / (RAND_MAX))*(2*mean);

return r;
}
tuple<double, double> get_new_customer(float teta=2.0,double timer=0){
double service=1;
double due=get_rnd_ex(teta)+timer;
return tuple<float, float>(service,due);
}

tuple<float, float> get_pd_pb(float mu=1.0,int q_cap=12,float teta_mean=2.0,float lambda=100){
// float service=;
// float due=;
int Customers=1*100000;
double timer=0;
long long d_counter=0;
long long b_counter=0;
double next_arrival=get_rnd_ex(1/lambda);
double next_departure=get_rnd_ex(1/lambda);
int next_departure_index=0;
bool debug=true;
vector<tuple<double, double>> q;
int i=0;
   while(i<Customers){
   
        //pop new costumer and add due,service
       
       if (q.size()>0){
        next_departure_index= rand() %q.size();
        next_departure=timer+get<0>(q[next_departure_index]);

       }
       else{
next_departure = std::numeric_limits<double>::max();

       }
      if (debug){

    cout << "timer__"<<timer<<"\n";
    cout << "dep__"<<next_departure<<"\n";
    cout << "arrival__"<<next_arrival<<"\n";
        //pop new arrival

      }
       
    if (next_arrival>next_departure){//departure
            q=update_due(q,next_departure-timer);
            timer=next_departure;
            q.erase(q.begin() + next_departure_index);
            d_counter+=1;
              if (debug){

            cout <<"d>>"<< timer<<"\n";
              }
    }
    else{//arrival

           if (q.size()==q_cap){
               //block
                b_counter+=1;
            }
            else 
            {
                //queue
                //service,due
                    tuple<double, double> customer=get_new_customer(2.0,timer);
                    //add to queue
                      if (debug){

    cout << "new C___due:"<< get<1>(customer)<<"service:_"<< get<0>(customer)<<"\n";
                      }
                    q.push_back(customer);
            }
        i++;
        q=update_due(q,next_arrival-timer);
        timer=next_arrival;
        next_arrival=timer+get_rnd_ex(1/lambda);
          if (debug){

            cout <<"a>>"<< timer<<"\n";
          }
    }

     
    }
    return tuple<float, float>(d_counter,b_counter);

}

int main(int argc, char** argv) {
    // cout << argv[0];
tuple<float, float> res=get_pd_pb();
 cout <<"d__"<<get<0>(res)<<"\n";
 cout << "b__"<<get<1>(res);

  return 0;
} 

