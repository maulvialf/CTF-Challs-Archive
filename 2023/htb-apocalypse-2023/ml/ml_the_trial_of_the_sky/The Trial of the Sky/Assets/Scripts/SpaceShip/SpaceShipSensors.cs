using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SpaceShipSensors : MonoBehaviour{
    public Transform spaceship;
    public float distance = 0;
    public float hitNormal = 0;

    

    private void Start(){
    }

    
    void LateUpdate(){

       
        Vector2 direction = gameObject.transform.position - spaceship.position;

       
        int layerMask1 = 1 << 8;
       
        int layerMask2 = 1 << 2;
        
        int layerMask = layerMask1 | layerMask2;
        
        layerMask = ~layerMask;
        hitNormal = 1;

       
        RaycastHit2D hit = Physics2D.Raycast(spaceship.position, direction, direction.magnitude, layerMask);
        if (hit.collider != null){

            
            hitNormal = hit.distance / direction.magnitude;

            Debug.DrawRay(spaceship.position, direction, Color.red);

            

        }else{
            distance = 1;
            Debug.DrawRay(spaceship.position, direction, Color.white);
           
        }

    }
}
