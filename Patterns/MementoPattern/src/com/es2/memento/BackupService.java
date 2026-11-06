package com.es2.memento;

import java.util.ArrayList;

public class BackupService {
    private Server server;
    private ArrayList<Memento> snapshots;

    public BackupService (Server server){
        this.server = server;
        this.snapshots = new ArrayList<>();
    }

    public void takeSnapshot() {
        Memento m = server.backup();
        snapshots.add(m);
    }

    public void restoreSnapshot(int snapshotNumber) throws NotExistingSnapshotException {
        if (snapshotNumber < 0 || snapshotNumber >= snapshots.size()) {
            throw new NotExistingSnapshotException();
        }
        Memento m = snapshots.get(snapshotNumber);
        server.restore(m);
    }
}
