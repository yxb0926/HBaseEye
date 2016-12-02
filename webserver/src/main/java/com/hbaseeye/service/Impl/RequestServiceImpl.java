package com.hbaseeye.service.Impl;

import com.hbaseeye.service.RequestService;
import com.mongodb.*;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Projections;
import org.bson.Document;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

import static com.mongodb.client.model.Filters.*;
import static com.mongodb.client.model.Projections.excludeId;
import static com.mongodb.client.model.Projections.fields;
import static com.mongodb.client.model.Projections.include;


/**
 * Created by yuanxiaobin on 16/12/2.
 */

@Service
public class RequestServiceImpl implements RequestService{

    public List getQps(String hostname, long starttime, long endtime) {
        final List list = new ArrayList();

        Block<Document> makeHashBlock = new Block<Document>() {
            public void apply(final Document document) {

                list.add(document.get("qps"));
            }
        };
        try{
            MongoClient mongoClient = new MongoClient("10.10.10.198", 27017);
            MongoDatabase mongoDatabase = mongoClient.getDatabase("hbasestat");

            MongoCollection<Document> collection = mongoDatabase.getCollection("regonRequest");

            collection.find(and(gt("timestamp",starttime),
                    eq("hostname",hostname))).
                    projection(new BasicDBObject("qps", true).append("_id", false)).forEach(makeHashBlock);

            mongoClient.close();

        } catch (Exception e){
            System.out.println(e);
        }

        return list;
    }

    public List getTps(String hostname, int timestamp) {
        return null;
    }

    public List getRead(String hostname, int timestamp) {
        return null;
    }

    public List getWrite(String hostname, int timestamp) {
        return null;
    }

    public List totalRequestCount(String hostname, int timestamp) {
        return null;
    }

    public List readRequestCount(String hostname, int timestamp) {
        return null;
    }

    public List writeRequestCount(String hostname, int timestamp) {
        return null;
    }
}
