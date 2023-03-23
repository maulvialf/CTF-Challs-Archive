using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class SpaceShipController : MonoBehaviour
{

    // Car properties
    public float acceleration = 5f;
    public float deacceleration = 3f;
    public float turnSpeed = 100f;
    public float speed;
    float torqueForce = 0;
    public SpaceShipCheckPoint spaceshipCheckPoint;
    int checkpointsPassed;
    Vector3 startingPos;
    Quaternion carRotation;
    float idleTime = 5f;
    float timeLeft = 0;
    int firstCheckpoint;

    
    float driftSpeedMoving = .9f;
   
    float driftSpeedStatic = .9f;
   
    float maxSideways = .5f;

   
    public Rigidbody2D spaceship;
    public List<SpaceShipSensors> sensors;

   
    public bool playerStopped;
    public bool playerHitWall;
    public bool hitCheckPoint;
    bool timerStarted;

    
    public float spaceshipDrive;
    public float spaceshipTurn;

    void Start(){
        
        spaceshipCheckPoint = gameObject.GetComponent<SpaceShipCheckPoint>();
        playerStopped = false;
        playerHitWall = false;
        hitCheckPoint = false;
        startingPos = gameObject.transform.position;
        carRotation = gameObject.transform.rotation;
        timerStarted = false;
        firstCheckpoint = spaceshipCheckPoint.nextCheckpoint;
        checkpointsPassed = 0;

    }

    void FixedUpdate(){
        speed = spaceship.velocity.magnitude;


        
        if (spaceship.velocity.magnitude < .05f){
            
            if (timerStarted){
                timeLeft += Time.deltaTime;
                if (timeLeft > idleTime){
            
                    playerStopped = true;
                    timerStarted = false;
                    timeLeft = 0;
                }
            }
            
            else{
                timerStarted = true;
            }
        }

        
        float driftFactor = driftSpeedStatic;
        if (ForwardVelocity().magnitude > maxSideways){
            driftFactor = driftSpeedMoving;
        }
        
        spaceship.velocity = ForwardVelocity() + SideVelocity() * driftFactor;

       
        if (spaceshipDrive >0){
            
            spaceship.AddForce(transform.up * acceleration);

        }
        if (Input.GetKey(KeyCode.S) || spaceshipDrive <= 0){
           
            spaceship.AddForce(transform.up * deacceleration);
        }

       
        torqueForce = Mathf.Lerp(0, turnSpeed, spaceship.velocity.magnitude / 2);
        
        spaceship.angularVelocity = (float)((spaceshipTurn) * torqueForce);

    }

    
    Vector2 ForwardVelocity(){
        
        return transform.up * Vector2.Dot(GetComponent<Rigidbody2D>().velocity, transform.up);
    }

    
    Vector2 SideVelocity(){
        return transform.right * Vector2.Dot(GetComponent<Rigidbody2D>().velocity, transform.right);
    }


    
    private void OnTriggerEnter2D(Collider2D other){
        if (other.gameObject.tag == "CheckPoint"){
            if (other.transform == spaceshipCheckPoint.checkpointArray[spaceshipCheckPoint.nextCheckpoint].transform)
            {
                

                if (checkpointsPassed + 1 == spaceshipCheckPoint.checkpointArray.Length)
                {
                    
                    spaceshipCheckPoint.nextCheckpoint = 18;
                    spaceshipCheckPoint.currentLap += 1;
                    checkpointsPassed = 1;
                }
                else
                {
                    
                    spaceshipCheckPoint.nextCheckpoint += 1;
                    spaceshipCheckPoint.nextCheckpoint = spaceshipCheckPoint.nextCheckpoint % 22;
                    checkpointsPassed += 1;
                    hitCheckPoint = true;
                }
            }
            return;
        }else if(other.gameObject.tag == "Player")
        {
            return;
        }
       

        playerHitWall = true;
       
    }

    public void ResetPosition(Vector3 startingPos, Quaternion rotation)
    {
        this.spaceship.velocity = Vector2.zero;
        this.spaceship.position = startingPos;
        gameObject.transform.rotation = rotation;
        this.spaceshipCheckPoint.nextCheckpoint = firstCheckpoint;
        timeLeft = 0;

        playerStopped = false;
        playerHitWall = false;
        hitCheckPoint = false;
        timerStarted = false;

    }

}
